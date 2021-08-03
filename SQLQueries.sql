############################################################################################################
# Part one
############################################################################################################
select date, sum (prod_qty * prod_price) as ventes
from (select distinct * from df_transaction)
where date >= '01/01/20' and date <= '31/12/20'
group by date
order by date

############################################################################################################
# Part two
############################################################################################################
select client_id,
       sum(case when product_type = 'MEUBLE' then (prod_price * prod_qty) end) as ventes_meuble,
       sum(case when product_type = 'DECO' then (prod_price * prod_qty) end)   as ventes_deco
from (select distinct *
      from df_transaction a
               join (select distinct * from df_product) b on a.prop_id = b.product_id)
where date >= '01/01/20' and date <= '31/12/20'
group by client_id