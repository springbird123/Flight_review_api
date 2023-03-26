# T2A2 API Webserver  

## R1 Identification of the problem you are trying to solve by building this particular app.
The problem this app aims to address is the lack of a centralized platform for users to share their flight experiences, search for flight reviews, and make informed decisions when booking future flights. This flight review API enables users to create and manage their accounts, post reviews about their flight experiences, and search for other people's reviews on specific flights. By providing this platform, users can easily access and contribute to a database of flight reviews, helping them make better decisions when selecting flights.

## R2 Why is it a problem that needs solving?  
The issue of limited access to flight experiences and reviews is a problem because it hinders informed decision-making and limits the ability to learn from others' experiences. When users lack access to the experiences of others, they may face difficulties in choosing the right flight based on their preferences and expectations. By having a centralized platform for flight reviews, users can make more informed decisions and select the best flight for their needs. Sharing flight experiences also can help users identify potential issues, areas for improvement, and commendable aspects of flights and airlines. Without a platform to share these experiences, users miss out on valuable insights that could help them make better travel decisions. Moverover, it also restricts the opportunity for airlines to receive feedback. Because flight reviews not only benefit passengers but also provide valuable feedback for airlines to identify areas for improvement and address any issues or concerns raised by their customers. 

## R3 Why have you chosen this database system. What are the drawbacks compared to others?
I chose PostgreSQL as the database management system. The reseasons I chose it including:

Open Source and Community Support: PostgreSQL is open source, which meansthat  it is freely available for use and modification. And the community around PostgreSQL is active and continuously contributes to its development, resulting in regular updates, new features, and extensive documentation.

ACID Compliance: PostgreSQL is ACID-compliant, ensuring data integrity and consistency across transactions. This is particularly important for applications dealing with sensitive data, such as user accounts and reviews.

Extensibility and Customizability: PostgreSQL supports custom functions, operators, and data types, allowing developers to extend the database system as needed. This flexibility makes it easier to adapt the database to the specific requirements of the application.

Concurrency Control: PostgreSQL implements a Multi-Version Concurrency Control (MVCC) mechanism, which allows multiple transactions to be in progress simultaneously without affecting each other's performance. This results in better performance and scalability, particularly in read-heavy applications.

Spatial Data Support: PostgreSQL, with its PostGIS extension, provides advanced support for spatial data and geographic objects, which could be useful for future extensions of the flight review API that may include geolocation features.

Drawbacks compared to other database systems:

Performance: PostgreSQL may have lower performance for certain workloads compared to some other databases, particularly those optimized for specific tasks or data types.

Complexity: PostgreSQL offers a wide range of features and customizability, which can make it more complex to set up and manage compared to simpler database systems.

## R4 Identify and discuss the key functionalities and benefits of an ORM  
An Object-Relational Mapping (ORM) is a technique that enables developers to map database tables and their relationships to objects in the programming language. The ORM provides a layer of abstraction between the application code and the database, which makes it easier to work with data.

Key functionalities and benefits of using an ORM includes:

Abstraction of database operations: With an ORM, developers don't have to write complex SQL queries to interact with the database. The ORM provides an abstraction layer that allows developers to work with objects instead of writing SQL statements. This can save a lot of development time and effort.

Object-oriented programming (OOP) principles: ORMs allow developers to use OOP principles in their database code. For example, they can define classes and objects that correspond to database tables and use inheritance and encapsulation to organize the code.

Database portability: ORMs provide an abstraction layer that isolates the application code from the database engine. This means that developers can switch to a different database engine without having to rewrite their code. They can also use the same code to work with multiple databases.

Improved performance: ORMs can help improve performance by caching data and minimizing database access. They can also optimize queries and transactions to reduce latency and increase throughput.

Easier testing: ORMs make it easier to write unit tests for database code. Since the ORM abstracts the database operations, developers can create mock objects to simulate database interactions and test the application code in isolation.

Reduced risk of SQL injection: By using an ORM, developers can avoid SQL injection attacks since the ORM is responsible for generating SQL statements and sanitizing user input.

Overall, using an ORM can help developers write cleaner, more maintainable code that is easier to test and less prone to errors. It can also save development time and effort by providing an abstraction layer that simplifies database interactions.

## Entity Relationship Diagram  

## Third Party Services  

## Project Models

## Database Relations  

##  Project Management  