import pandas as pd
import requests
import streamlit as st

class UMLSDBConnection:

    def __init__(self, apikey):
        self.api_key = apikey
        self.version = 'current'
        self.uri = "https://uts-ws.nlm.nih.gov"
        self.search_endpoint = self.uri + "/rest/search/" + self.version
        self.content_endpoint = self.uri + "/rest/content/" + self.version

    def query(self, term):
        params = {"string": term, "apiKey": self.api_key}
        response = requests.get(self.search_endpoint, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error querying the API. Status code: {response.status_code}")
            return None

    def get_snomedct_us_id(self, cui):
        params = {"apiKey": self.api_key}
        response = requests.get(f"{self.content_endpoint}/CUI/{cui}/atoms", params=params)
        
        if response.status_code == 200:
            data = response.json()
            atoms = data.get('result', [])
            
            for atom in atoms:
                if atom.get("rootSource") == "SNOMEDCT_US":
                    return atom.get("code").split('/')[-1]
        else:
            print(f"Error querying the API for source. Status code: {response.status_code}")

        return None

    def get_hierarchy(self, cui, relation_type):
        snomedct_us_id = self.get_snomedct_us_id(cui)
                
        if snomedct_us_id:
            params = {"apiKey": self.api_key}
            response = requests.get(f"{self.content_endpoint}/source/SNOMEDCT_US/{snomedct_us_id}/{relation_type}", params=params)
            
            if response.status_code == 200:
                data = response.json()
                # Display hierarchy data (update this part to properly display the data)
                # print(data)
                return data
            else:
                print(f"Error querying the hierarchy API. Status code: {response.status_code}")
                return None
        else:
            print("Failed to find SNOMEDCT_US ID for the given CUI.")
            return None


def display_json_data(json_data):
    results = json_data['result']['results']
    df = pd.DataFrame(results)
    st.dataframe(df[['name', 'ui', 'rootSource']])
    
def display_hierarchy_data(json_data):
    if json_data and "result" in json_data and json_data['result']:
        results = json_data['result']
        df = pd.DataFrame(results)
        st.dataframe(df)
    else:
        st.write("No hierarchy data available for this item.")

def main():
    st.title("UMLS API")
    api_key = 'dd59cd31-1a7a-4fb1-847a-7e03951a472c' #st.text_input("Enter your API Key", type="password")
    search_term = st.text_input("Enter your search term")
    relation_type = st.selectbox("Select the relation type", ["children", "parents", "ancestors", "descendants", "relations", "attributes"])

    if st.button("Search"):
        if not api_key or not search_term:
            st.warning("Please enter both the API Key and the search term.")
        else:
            conn = UMLSDBConnection(apikey=api_key)

            data = conn.query(search_term)

            if data:

                display_json_data(data)
                
                if data['result']['results']:
                    cui = data['result']['results'][0]['ui']
                    hierarchy_data = conn.get_hierarchy(cui, relation_type)

                    display_hierarchy_data(hierarchy_data)
                else:
                    st.error("Failed to find a relevant source for the CUI.")
            else:
                st.error("Failed to connect to UMLS API. Review API key and see logs.")

if __name__ == "__main__":
    main()
