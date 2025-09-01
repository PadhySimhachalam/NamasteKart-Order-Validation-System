import os
import datetime
import shutil
import csv
import File_Validation as v


def main():
    try:
        today_date = datetime.date.today().strftime('%Y%m%d')
        incoming_files_path = f'D:\\Python Programming\\Namastekart Project\\incoming_files\\{today_date}'
        success_files_path = f'D:\\Python Programming\\Namastekart Project\\success_files\\{today_date}'
        rejected_files_path = f'D:\\Python Programming\\Namastekart Project\\rejected_files\\{today_date}'

        incoming_files = os.listdir(incoming_files_path)
        total_cnt = len(incoming_files)

        if total_cnt > 0:
            success_cnt = 0
            rejected_cnt = 0

            for file in incoming_files:
                flag = True
                header_written = False
                products = v.get_product_id()

                with open(f'{incoming_files_path}/{file}', 'r', newline='') as file_reader:
                    reader = csv.DictReader(file_reader)
                    header = reader.fieldnames
                    rows = list(reader)

                    # Case 1: Empty file
                    if not rows:
                        if not os.path.exists(rejected_files_path):
                            os.makedirs(rejected_files_path, exist_ok=True)
                        shutil.copy(f'{incoming_files_path}/{file}', f'{rejected_files_path}/{file}')
                        with open(f'{rejected_files_path}/error_{file}', 'w', newline='') as error_writer:
                            error_writer.write("Empty file\n")
                        rejected_cnt += 1
                        continue

                # Case 2: Validate each order
                for order_dict in rows:
                    rejected_reason = ''

                    # Run validations
                    val_pid = v.product_id_validation(order_dict['product_id'], products)
                    val_od = v.date_validation(order_dict['order_date'])
                    val_city = v.check_city(order_dict['city'])
                    val_empty = v.check_empty(order_dict)
                    val_sales = v.sales_amount_validation(order_dict)

                    # Collect reasons for rejection
                    if not val_pid:
                        rejected_reason += f"Invalid product id {order_dict['product_id']};"
                    if len(val_empty) > 0:
                        empty_reject_reason = 'Columns ' + ','.join(val_empty) + ' are empty.'
                        rejected_reason += empty_reject_reason + ';'
                    if not val_od:
                        rejected_reason += f"Date {order_dict['order_date']} is a future date.;"
                    if not val_city:
                        rejected_reason += f"Invalid city {order_dict['city']};"
                    if not val_sales and val_pid:
                        rejected_reason += "Invalid Sales calculation."

                    # If valid → do nothing, else reject
                    if val_pid and val_od and val_city and len(val_empty) == 0 and val_sales:
                        continue
                    else:
                        row_str = ','.join(order_dict.values()) + ',' + rejected_reason.strip(',')
                        flag = False

                        if not os.path.exists(rejected_files_path):
                            os.makedirs(rejected_files_path, exist_ok=True)
                        shutil.copy(f'{incoming_files_path}/{file}', f'{rejected_files_path}/{file}')
                        rejected_cnt += 1

                        with open(f'{rejected_files_path}/error_{file}', 'a', newline='') as error_writer:
                            if not header_written:
                                error_writer.write(
                                    'order_id,order_date,product_id,quantity,sales,city,rejected_reason\n')
                                header_written = True
                            error_writer.write(row_str + '\n')

                # Case 3: If file has no rejected rows → success
                if flag:
                    if not os.path.exists(success_files_path):
                        os.makedirs(success_files_path, exist_ok=True)
                    shutil.copy(f'{incoming_files_path}/{file}', f'{success_files_path}/{file}')
                    success_cnt += 1

            #  Print summary (after loop finishes)
            print(f"Total Files: {total_cnt}")
            print(f"Successful Files: {success_cnt}")
            print(f"Rejected Files: {rejected_cnt}")

    except Exception as e:
        print(f"Error: {e}")


main()
