from .simple_report import SimpleReport


class CompleteReport(SimpleReport):

    def __product_count_by_company(products_list):
        qty_by_company_dict = dict()

        for product in products_list:
            if product["nome_da_empresa"] not in qty_by_company_dict:
                qty_by_company_dict[product["nome_da_empresa"]] = 0
            qty_by_company_dict[product["nome_da_empresa"]] += 1

        return qty_by_company_dict

    @staticmethod
    def generate(products_list):

        data_dict = CompleteReport.__product_count_by_company(products_list)
        data_tuples = list(data_dict.items())

        company_stock_count = ""

        for company, qty in data_tuples:
            company_stock_count += f"- {company}: {qty}\n"

        return (
             f"{SimpleReport.generate(products_list)}\n"
             f"Produtos estocados por empresa:\n"
             f"{company_stock_count}"
        )
