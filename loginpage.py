from time import sleep

import streamlit as st

from crud import reads_all_users

def login():
    with st.container(border=True):
        st.markdown('Welcome to the login page!')
        users = reads_all_users
        users = {user.name: user for user in users}
        user_name = st.selectbox(
            'select your user',
            list(users.keys())
        )
        
        password = st.text_input(
            'type your password',
            type='password'
        )
        if st.button('login'):
            user = users[user_name]
            if user.verifies_password(password):
                st.success('You are logged in with sucess!')
                st.session_state['user'] = user
                st.session_state['logged in'] = True
                sleep (1)
                st.rerun()
            else:
                st.error('Incorrect password. Please try again.')

def main():
    if not 'logged in' in st.session_state:
        st.session_state['logged in'] = False

    if not st.session_state['logged in']:
        login()
    else:
        st.markdown('Welcome to the WebApp!')

if __name__ == '__main__':
    main()