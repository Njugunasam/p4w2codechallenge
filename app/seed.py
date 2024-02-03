# app/seed.py

from app import create_app, db, Restaurant, Pizza, RestaurantPizza

# Create the Flask app
app = create_app()

#app's context
with app.app_context():
    restaurant1 = Restaurant(name='Pizzeria Uno', address='123 Main St')
    restaurant2 = Restaurant(name='Slice Heaven', address='456 Oak St')

    pizza1 = Pizza(name='Margherita',
                   ingredients='Tomato Sauce, Mozzarella, Basil')
    pizza2 = Pizza(name='Pepperoni',
                   ingredients='Tomato Sauce, Mozzarella, Pepperoni')

    db.session.add_all([restaurant1, restaurant2, pizza1, pizza2])
    db.session.commit()

    restaurant_pizza1 = RestaurantPizza(
        price=10.99, pizza_id=pizza1.id, restaurant_id=restaurant1.id)
    restaurant_pizza2 = RestaurantPizza(
        price=12.99, pizza_id=pizza2.id, restaurant_id=restaurant1.id)
    restaurant_pizza3 = RestaurantPizza(
        price=11.99, pizza_id=pizza1.id, restaurant_id=restaurant2.id)

    db.session.add_all(
        [restaurant_pizza1, restaurant_pizza2, restaurant_pizza3])
    db.session.commit()
