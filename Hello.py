# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    # st.write("# Welcome to Streamlit! 👋")

    # st.sidebar.success("Select a demo above.")

    st.markdown("""
    <script>    
    function CopyToClipboard(id)
    {
        var r = document.createRange();
        r.selectNode(document.getElementById(id));
        window.getSelection().removeAllRanges();
        window.getSelection().addRange(r);
        document.execCommand('copy');
        window.getSelection().removeAllRanges();
    }
    </script>    
    """, unsafe_allow_html=True)

    code = '''def hello(): **👈 Select a dem
    o from the sidebar**
    print("Hello, Streamlit!")'''
    st.code(code, language=None)

    m = st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: rgb(204, 49, 49);
    }
    </style>""", unsafe_allow_html=True)

    b = st.button("test")

    st.markdown(
        """
        <button onclick="CopyToClipboard('content');return false;">Copy Text</button>
        <p id="content">Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.
        **👈 Select a demo from the sidebar** to see some examples
        of what Streamlit can do!</p>
        """
        , unsafe_allow_html=True
    )

    content_assitant = ['Hello', 'Good here. How about you?']
    content_user = ['hi', 'how are you']
    # chat_history = ""
    # for i in range(len(content_assitant)):
    #     assistant_message = f"\n {content_assitant[i]}"
    #     user_message = f"\n {content_user[i]}"
    #     chat_history += f"""<div class='Assistant'><img src='https://www.ABC.com/assets/img/favicons/favicon-96x96.png' width='17'><span class='disclaimer'> CGA Chat:</span><a href='#' onclick="CopyToClipboard('cgaChat_h{i}');return false;">Copy Text</a><BR><BR><p id='cgaChat_h{i}'>{assistant_message}</p></div>"""
    #     chat_history += f"""<div class='You'>⚛️ <span class='disclaimer'>  You:</span><a href='#' onclick="CopyToClipboard('userChat_h{i}');return false;">Copy Text</a><BR><BR><P id='userChat_h{i}'>{user_message}</p></div>"""
    # st.markdown(
    #     chat_history
    #     , unsafe_allow_html=True
    # )

    for i in range(len(content_assitant)):
        assistant_message = f"\n {content_assitant[i]}"
        user_message = f"\n {content_user[i]}"
        chat_history = f"""<div class='Assistant'><img src='https://www.ABC.com/assets/img/favicons/favicon-96x96.png' width='17'><span class='disclaimer'> CGA Chat:</span></div>"""
        st.markdown(chat_history, unsafe_allow_html=True)
        st.code(assistant_message, language=None)
        chat_history = f"""<div class='You'>⚛️ <span class='disclaimer'>  You:</span></div>"""
        st.markdown(chat_history, unsafe_allow_html=True)
        st.code(user_message, language=None)
    


if __name__ == "__main__":
    run()
