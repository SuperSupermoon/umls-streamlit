import pandas as pd
import requests

import streamlit as st
from streamlit.connections import ExperimentalBaseConnection

class UMLSDBConnection(ExperimentalBaseConnection):

    def _connect(self, **kwargs) -> None:
        if 'apikey' in kwargs:
            self.api_key = kwargs["apikey"]
            version = 'current'
            uri = "https://uts-ws.nlm.nih.gov"
            self.endpoint = uri + "/rest/search/" + version
        else:
            raise Exception("Not API KEY passed!")

        return None

    @st.cache_data(ttl=3600)
    def query(_self, term: str):

        data = None

        try:
            # Make a GET request to the UMLS API
            params = {
                "string": term,
                "apiKey": _self.api_key
            }
            response = requests.get(_self.endpoint, params=params)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Process the response in JSON format
                data = response.json()
            else:
                print(f"Error querying the API. Status code: {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"Connection error: {e}")

        return data


def display_json_data(json_data):
    results = json_data['result']['results']
    df = pd.DataFrame(results)
    st.dataframe(df)

# Main Streamlit app
def main():
    st.title("UMLS API")
    st.image("img/logo.jpg", caption="Logo UMLS", use_column_width=True)

    # Input boxes for API Key and Search Term
    api_key = st.text_input("Enter your API Key", type="password")
    search_term = st.text_input("Enter your search term")

    # Button to trigger the API call
    if st.button("Search"):
        if not api_key or not search_term:
            st.warning("Please enter both the API Key and the search term.")
        else:
            conn = st.experimental_connection("UMLSdb", type=UMLSDBConnection, apikey=api_key)

            data = conn.query(search_term)

            if data == None:
                st.error("Fail to connect to UMLS API review API key and see logs")
            else:
                display_json_data(data)

if __name__ == "__main__":
    main()