import streamlit as st

def main():
    # Multi-language dictionary
    languages = {
        "English": {
            "title": "Waste Management Insights",
            "select_language": "Choose Language",
            "caption_1": "Correlation Matrix After Cleaning Data",
            "caption_2": "Global Waste Statistics",
            "caption_3": "OLS Regression Results",
            "caption_4": "Correlation Matrix for Carbon Intensity",
            "caption_5": "Correlation Matrix for Society"
        },
        "Spanish": {
            "title": "Perspectivas de la Gestión de Residuos",
            "select_language": "Elegir idioma",
            "caption_1": "Matriz de correlación después de la limpieza de datos",
            "caption_2": "Estadísticas globales de residuos",
            "caption_3": "Resultados de la regresión OLS",
            "caption_4": "Matriz de correlación para la intensidad de carbono",
            "caption_5": "Matriz de correlación para la sociedad"
        }
        # Add more languages as needed
    }

    # Select language
    st.sidebar.title("Settings")
    language = st.sidebar.selectbox("Choose Language", options=list(languages.keys()))

    # Set the title of the dashboard
    st.title(languages[language]["title"])

    # Image URLs (update with your actual URLs)
    image_urls = [
        ("https://raw.githubusercontent.com/atts234/hello-streamlit3/main/Picture1.png", languages[language]["caption_1"]),
        ("https://raw.githubusercontent.com/atts234/hello-streamlit3/main/Picture2.jpg", languages[language]["caption_2"]),
        ("https://raw.githubusercontent.com/atts234/hello-streamlit3/main/Picture3.png", languages[language]["caption_3"]),
        ("https://raw.githubusercontent.com/atts234/hello-streamlit3/main/Picture5.png", languages[language]["caption_4"]),
        ("https://raw.githubusercontent.com/atts234/hello-streamlit3/main/Picture6.png", languages[language]["caption_5"])
    ]

    # Display images in a two-column layout
    cols = st.columns(2)
    for idx, (img_url, caption) in enumerate(image_urls):
        with cols[idx % 2]:
            st.image(img_url, caption=caption)

if __name__ == "__main__":
    main()
