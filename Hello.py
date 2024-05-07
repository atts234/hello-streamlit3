import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

@st.experimental_memo
def load_data():
    public_health = pd.read_csv('https://raw.githubusercontent.com/atts234/hello-streamlit3/main/clean_public_health2.csv')
    soil = pd.read_csv('https://raw.githubusercontent.com/atts234/hello-streamlit3/main/clean_soil.csv')
    vehicles = pd.read_csv('https://raw.githubusercontent.com/atts234/hello-streamlit3/main/clean_discarded_vehicles2.csv')

    # Remove European Union entries from the data
    public_health = public_health[~public_health['Country'].str.contains("European Union")]
    soil = soil[~soil['Country'].str.contains("European Union")]
    vehicles = vehicles[~vehicles['Country'].str.contains("European Union")]

    return public_health, soil, vehicles

public_health, soil, vehicles = load_data()

country_translations = {
    'English': {country: country for country in public_health['Country'].unique()},
    'French': {
        'Belgium': 'Belgique', 'Bulgaria': 'Bulgarie', 'Czechia': 'Tchéquie',
        'Germany': 'Allemagne', 'Denmark': 'Danemark', 'Estonia': 'Estonie',
        'Ireland': 'Irlande', 'Greece': 'Grèce', 'Spain': 'Espagne',
        'France': 'France', 'Croatia': 'Croatie', 'Italy': 'Italie',
        'Cyprus': 'Chypre', 'Latvia': 'Lettonie', 'Lithuania': 'Lituanie',
        'Luxembourg': 'Luxembourg', 'Hungary': 'Hongrie', 'Malta': 'Malte',
        'Netherlands': 'Pays-Bas', 'Austria': 'Autriche', 'Poland': 'Pologne',
        'Portugal': 'Portugal', 'Romania': 'Roumanie', 'Slovenia': 'Slovénie',
        'Slovakia': 'Slovaquie', 'Finland': 'Finlande', 'Sweden': 'Suède',
        'Iceland': 'Islande', 'Norway': 'Norvège', 'Liechtenstein': 'Liechtenstein',
        'Switzerland': 'Suisse', 'United Kingdom': 'Royaume-Uni', 'Montenegro': 'Monténégro',
        'North Macedonia': 'Macédoine du Nord', 'Serbia': 'Serbie', 'Turkey': 'Turquie',
        'Bosnia and Herzegovina': 'Bosnie-Herzégovine', 'Kosovo': 'Kosovo'
    },
    'Spanish': {
        'Belgium': 'Bélgica', 'Bulgaria': 'Bulgaria', 'Czechia': 'Chequia',
        'Germany': 'Alemania', 'Denmark': 'Dinamarca', 'Estonia': 'Estonia',
        'Ireland': 'Irlanda', 'Greece': 'Grecia', 'Spain': 'España',
        'France': 'Francia', 'Croatia': 'Croacia', 'Italy': 'Italia',
        'Cyprus': 'Chipre', 'Latvia': 'Letonia', 'Lithuania': 'Lituania',
        'Luxembourg': 'Luxemburgo', 'Hungary': 'Hungría', 'Malta': 'Malta',
        'Netherlands': 'Países Bajos', 'Austria': 'Austria', 'Poland': 'Polonia',
        'Portugal': 'Portugal', 'Romania': 'Rumanía', 'Slovenia': 'Eslovenia',
        'Slovakia': 'Eslovaquia', 'Finland': 'Finlandia', 'Sweden': 'Suecia',
        'Iceland': 'Islandia', 'Norway': 'Noruega', 'Liechtenstein': 'Liechtenstein',
        'Switzerland': 'Suiza', 'United Kingdom': 'Reino Unido', 'Montenegro': 'Montenegro',
        'North Macedonia': 'Macedonia del Norte', 'Serbia': 'Serbia', 'Turkey': 'Turquía',
        'Bosnia and Herzegovina': 'Bosnia y Herzegovina', 'Kosovo': 'Kosovo'
    }
}


def main():
    st.sidebar.title("Settings")
    chosen_language = st.sidebar.selectbox("Choose Language", options=list(country_translations.keys()))

    variable_options = {
        'Public Health': ('Public health', public_health),
        'Soil': ('Soil', soil),
        'Discarded Vehicles': ('Discarded vehicles', vehicles)
    }

    selected_variable = st.sidebar.selectbox("Select a variable:", list(variable_options.keys()))
    column_name, data = variable_options[selected_variable]

    data['Country'] = data['Country'].map(country_translations[chosen_language])

    st.title(f"Impact of Environmental Factors on Society - {selected_variable}")

    plt.figure(figsize=(12, 8))
    sns.barplot(x=column_name, y='Country', data=data, estimator=np.sum, ci=None, palette='viridis')
    plt.title(f"Overview: {selected_variable} Values per Country")
    plt.xlabel(f"Total {selected_variable} Value")
    plt.ylabel("Countries")
    plt.xticks(rotation=90)
    st.pyplot(plt.gcf())

    country = st.selectbox("Select a country to view details:", data['Country'].unique())
    if country:
        filtered_data = data[data['Country'] == country]
        plt.figure(figsize=(12, 8))
        sns.barplot(x=column_name, y='Country', data=filtered_data, estimator=np.sum, ci=None, palette='viridis')
        plt.title(f"Detailed {selected_variable} Values for {country}")
        plt.xlabel(f"Total {selected_variable} Value")
        plt.ylabel("Countries")
        plt.xticks(rotation=90)
        st.pyplot(plt.gcf())

if __name__ == "__main__":
    main()
