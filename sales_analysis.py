import numpy as np
#Rows->Products , Columns->Months
sales=np.array([
    [12000,15000,13000,17000],#Product A
    [8000,9000,7500,8800],#Product B
    [20000,22000,21000,25000],#Product C
    [14000,16000,15000,16500]#Product D
])
products=["Product A","Product B","Product C","Product D"]
#Total and average sales per product
total_sales=np.sum(sales,axis=1)
average_sales=np.mean(sales,axis=1)
#Best and Worst performing Product
best_product_index=np.argmax(total_sales)
worst_product_index=np.argmin(total_sales)
#Target based performance
target=50000
underperforming=total_sales<target
print("-----SALES PERFORMANCE REPORT-----\n")
for i in range(len(products)):
    print(f"{products[i]}")
    print(f" Total Sales:{total_sales[i]}")
    print(f" Average Monthly Sales :{average_sales[i]:.2f}")
    print(f"Underperforming :{underperforming[i]}")
    print("-"*35)
print("Best Performing Product:",products[best_product_index])
print("Worst Performing Product:",products[worst_product_index])
#Total Revenue per month
monthly_avenue=np.sum(sales,axis=0)
best_month_index=np.argmax(monthly_avenue)
worst_month_index=np.argmin(monthly_avenue)
print("-------MONTH-WISE PERFORMANCE--------")
for i,rev in enumerate(monthly_avenue):
    print(f"Month {i+1}: Revenue={rev}")
print(f"Best Month: Month {best_month_index+1}")
print(f"Worst Month: Month{worst_month_index+1}")
#Contribution percentage per product
total_company_sales=np.sum(total_sales)
contribution=(total_sales/total_company_sales)*100
print("\n-------PRODUCT CONTRIBUTION (%)---------")
for i , percent in enumerate(contribution):
    print(f"{products[i]} contributes {percent:.2f}% of total sales ")
#Performance Labelling
performance_label=np.where(total_sales>=60000,"Excellent",np.where(total_sales>=50000,"Good","Needs Improvement"))
print("\n---------PRODUCT PERFORMANCE LABEL-------------")
for i, label in enumerate(performance_label):
    print(f"{products[i]}:{label}")
#Product Ranking
ranking=np.argsort(total_sales)[::-1]#descending order
print("\n ------------PRODUCT RANKING------------")
for rank,idx in enumerate(ranking,start=1):
    print(f"{rank}.{products[idx]}-Total Sales: {total_sales[idx]}")


