**Schema (PostgreSQL v13)**

    CREATE SCHEMA dannys_diner;
    SET search_path = dannys_diner;
    
    CREATE TABLE sales (
      "customer_id" VARCHAR(1),
      "order_date" DATE,
      "product_id" INTEGER
    );
    
    INSERT INTO sales
      ("customer_id", "order_date", "product_id")
    VALUES
      ('A', '2021-01-01', '1'),
      ('A', '2021-01-01', '2'),
      ('A', '2021-01-07', '2'),
      ('A', '2021-01-10', '3'),
      ('A', '2021-01-11', '3'),
      ('A', '2021-01-11', '3'),
      ('B', '2021-01-01', '2'),
      ('B', '2021-01-02', '2'),
      ('B', '2021-01-04', '1'),
      ('B', '2021-01-11', '1'),
      ('B', '2021-01-16', '3'),
      ('B', '2021-02-01', '3'),
      ('C', '2021-01-01', '3'),
      ('C', '2021-01-01', '3'),
      ('C', '2021-01-07', '3');
     
    
    CREATE TABLE menu (
      "product_id" INTEGER,
      "product_name" VARCHAR(5),
      "price" INTEGER
    );
    
    INSERT INTO menu
      ("product_id", "product_name", "price")
    VALUES
      ('1', 'sushi', '10'),
      ('2', 'curry', '15'),
      ('3', 'ramen', '12');
      
    
    CREATE TABLE members (
      "customer_id" VARCHAR(1),
      "join_date" DATE
    );
    
    INSERT INTO members
      ("customer_id", "join_date")
    VALUES
      ('A', '2021-01-07'),
      ('B', '2021-01-09');

---

**Query #1**

    /* --------------------
       Case Study Questions
       --------------------*/
    
    -- 1. What is the total amount each customer spent at the restaurant?
    -- 2. How many days has each customer visited the restaurant?
    -- 3. What was the first item from the menu purchased by each customer?
    -- 4. What is the most purchased item on the menu and how many times was it purchased by all customers?
    -- 5. Which item was the most popular for each customer?
    -- 6. Which item was purchased first by the customer after they became a member?
    -- 7. Which item was purchased just before the customer became a member?
    -- 8. What is the total items and amount spent for each member before they became a member?
    -- 9.  If each $1 spent equates to 10 points and sushi has a 2x points multiplier - how many points would each customer have?
    -- 10. In the first week after a customer joins the program (including their join date) they earn 2x points on all items, not just sushi - how many points do customer A and B have at the end of January?
    
    -- Example Query:
    
    Select
    	s.customer_id,
        SUM(m.price) as total
    from sales s
    INNER JOIN menu m
    ON s.product_id = m.product_id
    GROUP BY s.customer_id;

| customer_id | total |
| ----------- | ----- |
| B           | 74    |
| C           | 36    |
| A           | 76    |

---
**Query #2**

    
    
    
    SELECT
    	customer_id,
        COUNT(DISTINCT order_date) as total_visitas
    FROM 
    	Sales
    GROUP BY customer_id;

| customer_id | total_visitas |
| ----------- | ------------- |
| A           | 4             |
| B           | 6             |
| C           | 2             |

---
**Query #3**

    
    
    WITH customer_rank AS (
    SELECT
    	*,
    	ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY order_date ASC) as filas
    
    FROM
    	Sales)
        
        
    SELECT
    	c.customer_id as id_cliente,
    	m.product_name as nombre_producto
    FROM customer_rank c
    INNER JOIN menu m
    ON c.product_id = m.product_id
    WHERE filas = 1

| id_cliente | nombre_producto |
| ---------- | --------------- |
| A          | sushi           |
| B          | curry           |
| C          | ramen           |

---

[View on DB Fiddle](https://www.db-fiddle.com/f/2rM8RAnq7h5LLDTzZiRWcd/9159)
