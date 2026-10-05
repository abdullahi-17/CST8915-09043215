# CST8915 Lab 2: Algonquin Pet Store Part 2

**Student Name**: Abdullahi Omer
**Student ID**: 09043215
**Course**: CST8915 Full-stack Cloud-native Development
**Semester**: Fall 2026

---

## Demo Video

🎥 [Watch Demo Video](https://youtu.be/2liZb03qPic)

---

## Repositories

[Product Service Repository](https://github.com/abdullahi-17/product-service.git)

[Order Service Repository](https://github.com/abdullahi-17/order-service.git)

[Store Front Repository](https://github.com/abdullahi-17/store-front.git)

## Reflection Questions

### Configuration Changes

For the order-service and product-service, I moved configuration values such as ports and the RabbitMQ connection string into environment variables instead of keeping them directly in the code. I used .env files locally and added .env.example files to show the required variables without exposing actual values. For the Backing Services factor, I configured the order-service to connect to RabbitMQ through an environment variable, allowing RabbitMQ to run independently on its own VM instead of being tied directly to the application.

### Environment Variables

Environment variables are important because they keep configuration separate from the application code. This allows the same code to run in different environments, such as development or production, without having to modify the source code. It also prevents sensitive information, such as passwords and connection strings, from being hard-coded and potentially committed to GitHub.

### Separate Repositories

Having a separate repository for each microservice allows each service to be developed, updated, tested, and deployed independently. A change to the product-service, for example, does not require rebuilding or redeploying the order-service. This makes the application easier to maintain and allows individual services to be scaled or changed based on their own requirements.

---

## Challenges and Learnings (Optional)

---

## Acknowledgments

[Optional: Credit any resources, documentation, or people who helped you]
