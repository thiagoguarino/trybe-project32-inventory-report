from collections import Counter
from datetime import date


# file authorship: thiago guarino
class SimpleReport:

    def __products_data_lists(products_list):
        manuf_date_list, comp_name_list, exp_date_list = list(), list(), list()

        for product in products_list:
            if "nome_da_empresa" in product.keys():
                comp_name_list.append(product["nome_da_empresa"])

            if "data_de_validade" in product.keys():
                exp_date_list.append(product["data_de_validade"])

            if "data_de_fabricacao" in product.keys():
                manuf_date_list.append(product["data_de_fabricacao"])

        return {
            "exp_date_list": exp_date_list,
            "manuf_date_list": manuf_date_list,
            "company_name_list": comp_name_list,
         }

    @staticmethod
    def generate(products_list):

        data_dict = SimpleReport.__products_data_lists(products_list)

        manuf_dict, expiration_dict = dict(), dict()

        current_date = date.today()

        # Data de validade mais próxima: YYYY-MM-DD
        for exp_date in data_dict["exp_date_list"]:
            sliced = exp_date.split('-')
            period_date = date(int(sliced[0]), int(sliced[1]), int(sliced[2]))
            date_spread = period_date - current_date
            expiration_dict[exp_date] = date_spread

        temp_exp = min(expiration_dict.values())
        res_exp = [
            key
            for key in expiration_dict
            if expiration_dict[key] == temp_exp
        ]

        exp_date_report_out = res_exp[0]

        # Data de fabricação mais antiga: YYYY-MM-DD
        for manuf_date in data_dict["manuf_date_list"]:
            sliced = manuf_date.split('-')
            period_date = date(int(sliced[0]), int(sliced[1]), int(sliced[2]))
            date_spread = current_date - period_date
            manuf_dict[manuf_date] = date_spread

        temp_manu = max(manuf_dict.values())
        res_manu = [key for key in manuf_dict if manuf_dict[key] == temp_manu]

        manuf_date_report_out = res_manu[0]

        # Empresa com mais produtos: NOME DA EMPRESA
        company_report = Counter(data_dict["company_name_list"])
        company_report_out = company_report.most_common()

        return (
             f"Data de fabricação mais antiga: {manuf_date_report_out}\n"
             f"Data de validade mais próxima: {exp_date_report_out}\n"
             f"Empresa com mais produtos: {company_report_out[0][0]}"
        )
