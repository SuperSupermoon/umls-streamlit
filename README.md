# UMLS-Streamlit
 App that implements st.experimental_connection with UMLS API



## UMLS

The **Unified Medical Language System (UMLS)** is a knowledge representation framework developed by the U.S. National Library of Medicine (NLM) to facilitate the integration and retrieval of biomedical and clinical information from various sources. The UMLS serves as a valuable resource for researchers, healthcare professionals, and developers in the medical field.

Key Components

1. `Metathesaurus`: The Metathesaurus is the core component of UMLS, and it contains a vast collection of terms and concepts from various biomedical vocabularies and ontologies. It includes terms from sources like MeSH (Medical Subject Headings), SNOMED CT, RxNorm, LOINC, and many others. Each concept in the Metathesaurus is assigned a unique identifier known as the CUI (Concept Unique Identifier).

2. `Semantic Network`: The Semantic Network is a hierarchy of semantic types and relationships that provide a structure for organizing and understanding the concepts in the Metathesaurus. It classifies concepts into categories based on their meaning and relationships with other concepts.

3. `Lexical Tools`: UMLS provides lexical tools to support natural language processing tasks, such as lemmatization, stemming, and word normalization, which help improve the quality and accuracy of text processing in the biomedical domain.

4. `APIs and Services`: UMLS offers APIs and web services that allow developers to access and query the UMLS data programmatically, making it easier to integrate UMLS into their applications and research.

```
Bodenreider O. The Unified Medical Language System (UMLS): integrating biomedical terminology. 
Nucleic Acids Res. 2004 Jan 1;32(Database issue):D267-70. doi: 10.1093/nar/gkh061.
PubMed PMID: 14681409; PubMed Central PMCID: PMC308795.
```
# umls-streamlit
