#--------------------------------------------------#
#   To run Enter Command "streamlit run main.py"   #
#--------------------------------------------------#
import streamlit as st
import mysql.connector

# Connect to MySQL database
mysql = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password",
    database="hotel1"
)

# Initialize cursor
cursor = mysql.cursor()

# Function to insert order details into the database
def insert_order(order_id, dish_numbers, quantities, total_bill, discount):
    for dish_number, quantity in zip(dish_numbers, quantities):
        bill_amount = calculate_bill(dish_number, quantity)
        query = "INSERT INTO hotel (order_id, dish_number, quantity, bill_amount, discount, total_bill) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (order_id, dish_number, quantity, bill_amount, discount, total_bill)
        cursor.execute(query, values)
    mysql.commit()

# Function to calculate bill based on dish and quantity
def calculate_bill(dish_number, quantity):
    if dish_number == 1:
        return 60 * quantity
    elif dish_number == 2:
        return 70 * quantity
    elif dish_number == 3:
        return 50 * quantity
    elif dish_number == 4:
        return 60 * quantity
    else:
        return 0

# Streamlit app
st.markdown("<h1 style='text-align: center;'>Welcome to Hotel Rajeshahi!</h1>", unsafe_allow_html=True)

# Display menu
st.markdown("<h3 style='text-align: center;'>Rajesahi Menu</h3>", unsafe_allow_html=True)
col1, col2 = st.columns([1, 1])
with col1:
    st.markdown("<h5 style='text-align: left; padding-left:28px'>Dishes</h5>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: left; padding-left:5px'><span style='margin-right:10px'>1.</span>Maharashtraian Tali</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: left; padding-left:5px'><span style='margin-right:10px'>2.</span>Rajestani Tali</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: left; padding-left:5px'><span style='margin-right:10px'>3.</span>IDLI DOSA</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: left; padding-left:5px'><span style='margin-right:10px'>4.</span>Sweets\n</p>", unsafe_allow_html=True)
with col2:
    st.markdown("<h5 style='text-align: right;'>Price/-</h5>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: right; margin-right:25px'; >60</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: right; margin-right:25px'; >70</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: right; margin-right:25px'; >50</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: right; margin-right:25px'; >60</p>", unsafe_allow_html=True)

# Initialize order ID
order_id = 1

while True:
    dish_numbers = []
    quantities = []

    order_select_key = f"order_select_{order_id}"
    name = st.selectbox(f"Do you want to order? (Order {order_id})", ["Yes", "No"], key=order_select_key)

    if name == "Yes":
        order_count = 0

        while name == "Yes":
            order_count += 1

            dish_key = f"dish_{order_id}_{order_count}"
            quantity_key = f"quantity_{order_id}_{order_count}"

            dish_number = st.number_input(f"Enter the dish number {order_count} (Order {order_id}):", min_value=1, max_value=4, key=dish_key)
            quantity = st.number_input(f"Enter the quantity {order_count} (Order {order_id}):", min_value=1, key=quantity_key)

            dish_numbers.append(dish_number)
            quantities.append(quantity)

            new_order_key = f"new_Order_{order_id}_{order_count}"
            name = st.selectbox(f"Do you want to order more? (Order {order_id})", ["No", "Yes"], key=new_order_key)

            # Check if the user wants to continue ordering
            if name == "No":
                break  # Exit the inner while loop

        if dish_numbers:
            print_bill_key = f"print_Bill_{order_id}"
            if st.button(f"Print Bill for Order", key=print_bill_key):
                total = sum(calculate_bill(dish_number, quantity) for dish_number, quantity in zip(dish_numbers, quantities))
                if 100 < total < 200:
                    discount = 0.05 * total
                elif 200 < total < 500:
                    discount = 0.07 * total
                elif total > 500:
                    discount = 0.10 * total
                else:
                    discount = 0

                total_bill = total - discount

                st.markdown("<h4 style='text-align: center;'>Bill Details</h4>", unsafe_allow_html=True)
                st.write("--------------------------------------------------")
                col5, col6, col7 = st.columns([1, 1, 1]) 
                with col5:
                    st.markdown("<h5 style='text-align: left; padding-left:28px'>Dish</h5>", unsafe_allow_html=True)
                    st.write("----------------------------------------------------------------------------")
                with col6:
                    st.markdown("<h5 style='text-align: left; padding-left:100px'>Qty</h5>", unsafe_allow_html=True)
                    st.write("--------------------------------------------------")
                with col7:
                    st.markdown("<h5 style='text-align: right;'>Value</h5>", unsafe_allow_html=True)
                    st.write("--------------------------------------------------")

                for dish_number, quantity in zip(dish_numbers, quantities):
                    dish_name = {
                        1: "Maharashtraian Tali",
                        2: "Rajestani Tali",
                        3: "IDLI DOSA",
                        4: "Sweets"
                    }[dish_number]
                    value = calculate_bill(dish_number, quantity)
                    st.markdown(f"<h5 style='text-align: left'>{dish_name}<span style='text-align: left; margin-left:200px'>{quantity}</span><span style='text-align: left; margin-left:300px'>{value}</span></h5>", unsafe_allow_html=True)
                st.write("--------------------------------------------------")

                st.write("Bill:", total)
                st.write("Discount:", discount)
                st.write("Total Bill:", total_bill)

                insert_order(order_id, dish_numbers, quantities, total_bill, discount)

                # Increase order_id for the next order
                order_id += 1

    if name == "No":  # Check if the user wants to continue ordering
        break  # Exit the outer while loop

# Explicitly close the MySQL connection
mysql.close()
