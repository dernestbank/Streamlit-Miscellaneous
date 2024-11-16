import streamlit as st
from streamlit_option_menu import option_menu



import about , account, home, login, signup

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
)


class Multiapp:
    def __init__(self):
        self.apps = []
    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        
        with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",
                options=["Home", "Login", "Signup", "Account", "About"],
                icons=["house", "person", "person-plus", "key", "book"],
                menu_icon="cast",
                default_index=0,
                orientation="horizontal",
                styles={
                    "container": {"padding": "0!important", "background-color": "#fafafa"},
                    "icon": {"color": "orange", "font-size": "25px"},
                    "nav-link": {
                        "font-size": "16px",
                        "text-align": "left",
                        "margin": "0px",
                        "--hover-color": "#eee",
                    },
                    "nav-link-selected": {"background-color": "green"},
                }
            )
            
        if app == "Home":
            home.app()
        if app == "Login":
            login.app()
        if app == "Signup":
            signup.app()
        if app == "Account":
            account.app()
        if app == "About":
            about.app()
            
            
    # run()
    Multiapp().run()
        
        
 
        
        
        # app = st.sidebar.selectbox(
        #     'Navigation',
        #     self.apps,
        #     format_func=lambda app: app['title'])

        # app['function']()
        
        
        


# if __name__ == '__main__':
#     main()

    