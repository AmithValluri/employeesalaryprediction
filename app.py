import streamlit as st
import pandas as pd

def main():
    """
    This function defines the Streamlit application layout and logic.
    It allows users to upload a CSV file and displays its content.
    """
    st.set_page_config(layout="wide") # Use wide layout for better data display
    st.title("CSV Data Viewer")
    st.markdown("Upload a CSV file to view its contents and basic information.")

    # File uploader widget
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        try:
            # Read the uploaded CSV file into a pandas DataFrame
            # st.cache_data is used to cache the data loading,
            # so it doesn't reload every time the app reruns.
            df = pd.read_csv(uploaded_file)

            st.success("CSV file loaded successfully!")

            # Display the first few rows of the DataFrame
            st.subheader("Data Preview (First 5 Rows):")
            st.dataframe(df.head()) # Use st.dataframe for interactive table display

            # Display basic information about the DataFrame
            st.subheader("DataFrame Information:")
            # Create a string buffer to capture df.info() output
            from io import StringIO
            buffer = StringIO()
            df.info(buf=buffer)
            s = buffer.getvalue()
            st.text(s) # Display the captured info as preformatted text

            # Display descriptive statistics
            st.subheader("Descriptive Statistics:")
            st.dataframe(df.describe())

            # Optional: Allow user to view the full DataFrame
            if st.checkbox("Show full DataFrame"):
                st.subheader("Full DataFrame:")
                st.dataframe(df)

        except Exception as e:
            st.error(f"An error occurred while processing the CSV file: {e}")
            st.warning("Please ensure the uploaded file is a valid CSV and correctly formatted.")
    else:
        st.info("Please upload a CSV file to get started.")

if __name__ == "__main__":
    main()
