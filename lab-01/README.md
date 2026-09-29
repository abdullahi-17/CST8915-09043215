# CST8915 Lab 1: Algonquin Pet Store on Azure VM

**Student Name**: Abdullahi Omer
**Student ID**: 09043215
**Course**: CST8915 Full-stack Cloud-native Development
**Semester**: Fall 2026

---

## Demo Video

🎥 [Watch Demo Video](https://youtu.be/jMIohTiHoyk)

---

## Technical Explanations

### Order Service (Node.js)

The Order Service takes in customer orders. It exposes one endpoint, POST /orders, on port 3000. The endpoint accepts a JSON body with product, quantity and totalPrice, and hands it off for processing later instead of processing it right away. It is written in Node.js, an open-source backend technology that creates a runtime environment, allowing users to run JavaScript code on a server or a local computer, instead of only inside a web browser. It acts as a bridge between client-side and server-side programming.

Within the architecture, the Order Service is the producer side of an asynchronous messaging pattern. When an order arrives, it connects to RabbitMQ and creates a confirm channel. It declares order_queue and publishes the order. The HTTP response is sent only after the broker confirms it received the message. The service never calls the Product Service; it trusts the product data the front end sends.

### Product Service (Rust)

The Product Service provides the store's product catalog. It exposes products on port 3030 and returns a JSON array of products with id, name and price: Dog Food, Cat Food and Bird Seeds. The service is written in Rust, a programming language that emphasizes performance, type safety, concurrency, and memory safety. Rust provides memory safety without a garbage collector and produces a small native binary with low latency and a small footprint. Those are good traits for a read-heavy catalog that many clients may hit at once.

Within the architecture, the Product Service is a stateless, read-only service that owns the product domain. Because it's stateless, it's easy to replicate and scale separately from the rest of the system, and it could later be backed by a real database without the other services noticing. It communicates only through synchronous HTTP/REST. It makes no outbound calls and doesn't use RabbitMQ. Its only client is the Store Front, which fetches the catalog when the page loads.

### Store Front (Vue.js)

The Store Front is the customer-facing web interface. Customers see the Algonquin Pet Store page, pick a product, enter a quantity, see a live total, and place an order. It has a single-page application created through Vue.js, used for building frontend user interfaces with JacaScript, CSS, and HTML. It uses built-in and user defined directives to offer functionality to HTML elements. Vue fits here because it's lightweight, uses components and handles reactivity.

Within the architecture, the Store Front is the presentation layer and acts as the client-side aggregator of the two backend services. It has no backend of its own: the browser calls each service directly over HTTP using fetch, then sends a GET request to the Product Service to fill the product list. When the user clicks "Place Order", it sends POST to the Order Service with the selected product, quantity and total. It never talks to RabbitMQ; the Order Service hides the messaging layer behind a plain REST call.

---

## Challenges and Learnings (Optional)

This lab has helped me familiarize myself more with the Azure platform and configuring different settings for resource groups and vms. I also deepend my knowledge in remote configurations and hands on practice with combining different components to create a full stack application, as well as getting them to communicate with each other.

One big challenge I faced was during the setup of the pet-store vm. Due to the limitations that come with the Axure for Students subscription, I was unable to use the region and disk size that was recommended in the lab instructions. Instead, I chose the smallest and cheapest disk size available. What I then noticed while continuing through the lab was that I was unable to SSH into my VM, through VsCode or my local terminal. The remote access would initially connect, then disconnect after less than 30 seconds. I first checked my network configurations on Azure and my settings on VsCode and could not determine the root cause. I then decided to use AI for support, but even that didn't help. I used 4 different AI agents, including Copilot on Azure. After 4 hours of trial and error and using a lot credits, I decided to look into the VM's configuration. That's when I noticed that the disk size had only 2 VCPU's while the majority of the other disk size options start at 4. I then resized the VM, and luckily enough, the remote SSH worked on the first try.

---

## Acknowledgments

[Optional: Credit any resources, documentation, or people who helped you]

```
https://www.w3schools.com/nodejs/nodejs_intro.asp
https://www.sanity.io/glossary/vue-js
https://www.w3schools.com/rust/rust_intro.php

---
```
