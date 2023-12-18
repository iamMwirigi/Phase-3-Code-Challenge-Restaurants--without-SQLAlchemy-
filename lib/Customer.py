class Customer:
    customers = []

    def __init__(self, given_name, family_name):
        # Initialize Customer instance with given name, family name, and an empty reviews list
        self.given_name = given_name
        self.family_name = family_name
        self.reviews_list = []
        # Add the new customer instance to the list of all customers
        Customer.customers.append(self)

    def given_name(self):
        return self.given_name

    def family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def all(cls):
        # Return a list of all customer instances
        return cls.customers

    def add_review(self, review):
        # Add a review to the customer's reviews list
        self.reviews_list.append(review)


class Restaurant:
    restaurants = []

    def __init__(self, name):
        # Initialize Restaurant instance with a name and an empty reviews list
        self.name = name
        self.reviews_list = []
        # Add the new restaurant instance to the list of all restaurants
        Restaurant.restaurants.append(self)

    def __str__(self):
        # Return the name of the restaurant when the instance is converted to a string
        return self.name

    def name(self):
        return self.name

    def reviews(self):
        # Return the list of reviews for the restaurant
        return self.reviews_list

    def customers(self):
        # Return a list of unique customers who have reviewed the restaurant
        return list(set(review.customer() for review in self.reviews_list))

    def average_star_rating(self):
        if not self.reviews_list:
            return 0
        # Calculate the average star rating for the restaurant based on its reviews
        total_ratings = sum(review.rating() for review in self.reviews_list)
        return total_ratings / len(self.reviews_list)


class Review:
    reviews = []

    def __init__(self, customer, restaurant, rating):
        # Initialize Review instance with a customer, restaurant, and rating
        self.customer = customer
        self.restaurant = restaurant
        self.rating_value = rating
        # Add the new review instance to the lists of customer and restaurant reviews
        self.customer.add_review(self)
        self.restaurant.reviews_list.append(self)
        # Add the new review instance to the list of all reviews
        Review.reviews.append(self)

    def rating(self):
        # Return the rating value for the review
        return self.rating_value

    @classmethod
    def all(cls):
        # Return a list of all review instances
        return cls.reviews

    def customer(self):
        # Return the customer object for the review
        return self.customer

    def restaurant(self):
        # Return the restaurant object for the review
        return self.restaurant

if __name__ == "__main__":
    # Example tests
    customer1 = Customer("John", "Doe")
    restaurant1 = Restaurant("Sample Restaurant")
    review1 = Review(customer1, restaurant1, 4)

    print(customer1.full_name())  # Output: John Doe
    print(str(Restaurant.restaurants[0]))  # Output: Sample Restaurant
    print(review1.rating())  # Output: 4
    print(Restaurant.restaurants[0].average_star_rating())  # Output: 4.0