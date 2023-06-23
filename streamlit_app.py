import streamlit as st
from resume_parser import resumeParser

obj = resumeParser()


def app():
    st.set_page_config(page_title='Resume Miner',
                       page_icon=':clipboard:', layout='wide')
    st.title('Resume Miner :sleuth_or_spy:')

    # Add a file uploader to allow the user to upload a resume
    uploaded_file = st.sidebar.file_uploader('##### Upload a resume in PDF format :arrow_up_small:', type=[
                                              'pdf', 'docx'], )


    # If a file has been uploaded, parse it and display the results
    if uploaded_file is not None:
        try:
            dict = None
            with st.spinner('Analyzing resume... :mag_right::hourglass_flowing_sand:'):
                dict = obj.extract_data_from_file(uploaded_file)

                with st.expander(f' Name: **dict["name"]** '):
                    st.markdown(
                        f'**Email:** dict["email"] :envelope_with_arrow:')
                    st.markdown(
                        f'**Highlights:** dict["phone"] :star2:')
                    st.markdown('#### **Skills:** ')
                    for i in dict["skills"].split(','):
                        st.markdown(f'* {i} ')

        except Exception as e:
            st.write('Error: Unable to parse the resume ', e)


# Run the Streamlit app
if __name__ == '__main__':
    app()
