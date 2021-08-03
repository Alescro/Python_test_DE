--- First Query

select date, sum(prod_price * prod_qty) AS ventes
FROM (select distinct * from transactions) AS T WHERE date BETWEEN ('01/01/19') AND ('31/12/19')
GROUP BY date ORDER BY date ASC;


--- Second Complex Query

SELECT client_id,
    sum(CASE WHEN product_type = 'MEUBLE' THEN prod_price * prod_qty END) AS ventes_meuble,
    sum(CASE WHEN product_type = 'DECO' THEN prod_price * prod_qty END) AS ventes_deco

FROM (
    select *
    FROM transactions t INNER JOIN product_nomenclature p
    ON t.prod_id = p.product_id WHERE date BETWEEN ('01/01/19') AND ('31/12/19')
) as t

GROUP BY client_id