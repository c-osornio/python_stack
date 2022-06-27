-- Complete the below SQL queries using the lead-gen-business-new database
USE lead_gen_business;
-- 1. What query would you run to get the total revenue for March of 2012?
SELECT DATE_FORMAT(charged_datetime, '%M') AS month, SUM(amount) AS revenue
FROM billing
WHERE charged_datetime LIKE "2012-03%";
-- 2. What query would you run to get total revenue collected from the client with an id of 2?
SELECT client_id, SUM(amount) AS total_revenue
FROM billing
WHERE client_id = 2;
-- 3. What query would you run to get all the sites that client with an id of 10 owns?
SELECT domain_name AS website, client_id
FROM sites
WHERE client_id = 10;
-- 4a. What query would you run to get total # of sites created per month per year for the client with an id of 1? What about for client with an id of 20?
SELECT client_id, COUNT(domain_name) AS number_of_websites, DATE_FORMAT(created_datetime, '%M') AS month_created, DATE_FORMAT(created_datetime, '%Y') AS year_created
FROM sites
WHERE client_id = 1
GROUP BY MONTH(created_datetime), YEAR(created_datetime);
-- 4b. What about for client with an id of 20?
SELECT client_id, COUNT(domain_name) AS number_of_websites, DATE_FORMAT(created_datetime, '%M') AS month_created, DATE_FORMAT(created_datetime, '%Y') AS year_created
FROM sites
WHERE client_id = 20
GROUP BY MONTH(created_datetime), YEAR(created_datetime);
-- 5. What query would you run to get the total # of leads generated for each of the sites between January 1, 2011 to February 15, 2011?
SELECT domain_name AS website, COUNT(leads_id) AS number_of_leads
FROM sites
JOIN leads
ON sites.site_id = leads.site_id
WHERE registered_datetime BETWEEN "2011-01-01%" AND "2011-02-15%"
GROUP BY domain_name;
-- 6. What query would you run to get a list of client names and the total # of leads we've generated for each of our clients between January 1, 2011 to December 31, 2011?
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client, COUNT(leads_id) AS number_of_leads
FROM clients
JOIN sites
ON clients.client_id = sites.client_id
JOIN leads
ON sites.site_id = leads.site_id
WHERE registered_datetime BETWEEN "2011-01-01%" AND "2011-12-31%"
GROUP BY client;
-- 7. What query would you run to get a list of client names and the total # of leads we've generated for each client each month between months 1 - 6 of Year 2011?
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client, COUNT(leads_id) AS number_of_leads, DATE_FORMAT(registered_datetime, '%M') AS month_generated
FROM clients
JOIN sites
ON clients.client_id = sites.client_id
JOIN leads
ON sites.site_id = leads.site_id
WHERE registered_datetime BETWEEN "2011-01-01%" AND "2011-06-30%"
GROUP BY leads_id;
-- 8. What query would you run to get a list of client names and the total # of leads we've generated for each of our clients' sites between January 1, 2011 to December 31, 2011? Order this query by client id.
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client, domain_name AS website, COUNT(leads_id) AS number_of_leads
FROM clients
JOIN sites
ON clients.client_id = sites.client_id
JOIN leads
ON sites.site_id = leads.site_id
WHERE registered_datetime BETWEEN "2011-01-01%" AND "2011-12-31%"
GROUP BY domain_name
ORDER BY clients.client_id;
--  Come up with a second query that shows all the clients, the site name(s), and the total number of leads generated from each site for all time.
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client, domain_name AS website, COUNT(leads_id) AS number_of_leads
FROM clients
JOIN sites
ON clients.client_id = sites.client_id
JOIN leads
ON sites.site_id = leads.site_id
GROUP BY domain_name
ORDER BY clients.client_id;
-- 9a. Write a single query that retrieves total revenue collected from each client for each month of the year. Order it by client id.  First try this with integer month
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, SUM(amount) AS total_revenue, DATE_FORMAT(charged_datetime, '%m') AS month_charged, DATE_FORMAT(charged_datetime, '%Y') AS year_charged
FROM clients
JOIN billing
ON clients.client_id = billing.client_id
GROUP BY month_charged, clients.client_id
ORDER BY clients.client_id;
-- 9b. Second with month name.  A SELECT subquery will be needed for the second challenge. 
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, SUM(amount) AS total_revenue, DATE_FORMAT(charged_datetime, '%M') AS month_charged, DATE_FORMAT(charged_datetime, '%Y') AS year_charged
FROM clients
JOIN billing
ON clients.client_id = billing.client_id
GROUP BY month_charged, clients.client_id
ORDER BY clients.client_id;
-- 10. Write a single query that retrieves all the sites that each client owns. Group the results so that all of the sites for each client are displayed in a single field. It will become clearer when you add a new field called 'sites' that has all the sites that the client owns. (HINT: use GROUP_CONCAT)
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, GROUP_CONCAT(domain_name SEPARATOR ' / ') AS sites
FROM clients
LEFT JOIN sites
ON clients.client_id = sites.client_id
GROUP BY clients.client_id;