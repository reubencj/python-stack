use world;
-- 1. What query would you run to get all the countries that speak Slovene? Your query should return the name of the country,
-- language and language percentage. Your query should arrange the result by language percentage in descending order. (1)
select
  c.name,
  l.language,
  l.percentage
from
  countries c
  join languages l on l.country_code = c.code
where
  l.language = 'Slovene'
order by
  l.percentage desc;
-- 2. What query would you run to display the total number of cities for each country?
  --Your query should return the name of the country and the total number of cities.
  --Your query should arrange the result by the number of cities in descending order. (3)
select
  c.name,
  COUNT(ci.name)
from
  countries c
  join cities ci on c.code = ci.country_code
GROUP BY
  1
order by
  2 desc;
-- 3. What query would you run to get all the cities in Mexico with a population of greater than 500,000?
  --Your query should arrange the result by population in descending order. (1)
select
  ci.name
from
  countries c
  join cities ci on c.code = ci.country_code
where
  c.name = 'Mexico'
  and ci.population > 500000
ORDER BY
  ci.population DESC;
-- 4. What query would you run to get all languages in each country with a percentage greater than 89%?
  --Your query should arrange the result by percentage in descending order. (1)
select
  c.name,
  l.language,
  l.percentage
from
  countries c
  join languages l on l.country_code = c.code
where
  l.percentage >= 90
order by
  l.percentage desc;
-- 5. What query would you run to get all the countries with Surface Area below 501 and Population greater than 100,000? (2)
select
  *
from
  countries
where
  surface_area < 501
  and population > 100000;
-- 6. What query would you run to get countries with only Constitutional Monarchy
  --with a capital greater than 200 and a life expectancy greater than 75 years? (1)
select
  *
from
  countries
where
  government_form = 'Constitutional Monarchy'
  and capital > 200
  and life_expectancy > 75;
-- 7. What query would you run to get all the cities of Argentina inside the Buenos Aires district
  --and have the population greater than 500, 000? The query should return the Country Name, City Name, District and Population. (2)
select
  c.name,
  ci.name,
  ci.district,
  ci.population
from
  countries c
  join cities ci on c.code = ci.country_code
where
  ci.district = 'Buenos Aires'
  and ci.population > 500000;
-- 8. What query would you run to summarize the number of countries in each region?
  --The query should display the name of the region and the number of countries. Also, the query should arrange the result
  --by the number of countries in descending order. (2)
select
  region,
  COUNT(c.name) no_of_countries
from
  countries c
group by
  1
ORDER BY
  COUNT(c.name) desc;