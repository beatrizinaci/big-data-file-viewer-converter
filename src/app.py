import streamlit as st
import file_manager
import os


def display_file_options(file_options, file_name):
    if file_options:
        st.write("**Custom options:**")

        columns = st.columns(len(file_options))

        for col, (option, default_value) in zip(columns, file_options.items()):
            with col:            
                unique_id = f"{file_name}_{option}"        
                if option == "header":  
                    use_header = st.checkbox("CSV has header", value=(default_value == 0), key=unique_id)
                    file_options[option] = 0 if use_header else None
                elif isinstance(default_value, str):  
                    file_options[option] = st.text_input(f"{option.capitalize()}:", default_value, key=unique_id)
                elif isinstance(default_value, int):  
                    file_options[option] = st.number_input(f"{option.capitalize()}:", min_value=-1, value=default_value, step=1, key=unique_id)
                elif isinstance(default_value, bool):  
                    file_options[option] = st.checkbox(f"{option.capitalize()}:", value=default_value, key=unique_id)
    

def process_uploaded_files(uploaded_files):
    for uploaded_file in uploaded_files:
        file_type = os.path.splitext(uploaded_file.name)[1]
        st.write(f"###  {uploaded_file.name}")

        if not file_manager.is_supported(file_type):
            st.error(f"File format {file_type} not supported")
            continue

        file_options = file_manager.FILE_HANDLERS[file_type]["options"].copy()
        display_file_options(file_options, uploaded_file.name)

        try:
            df = file_manager.read_file(uploaded_file, file_type, **file_options)
        except Exception as e:
            st.error(f"Error reading {uploaded_file.name}: {e}")
            continue
        else:
            if df is not None:
                st.write(df)
            else:
                st.error(f"Error reading {uploaded_file.name}")

        st.divider()    


def main():
    st.title("Big data file converter")
    st.info(f"Accepeted formats: {','.join(file_manager.FILE_HANDLERS.keys())}")

    uploaded_files = st.file_uploader("Upload a file", accept_multiple_files=True)
    
    if uploaded_files:
        process_uploaded_files(uploaded_files)

if __name__ == "__main__":
    main()