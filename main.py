import streamlit as st
import langchainhelper

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Select a cuisine", ("Italian", "French", "Mexican", "Indian"))


if cuisine:
    response = langchainhelper.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")

    st.write(""" *** MENU ITEMS ***""")
    for item in menu_items:
        st.write(item)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
