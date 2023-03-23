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

## Entity Relationship Diagram  

## Third Party Services  

## Project Models

## Database Relations  

##  Project Management  