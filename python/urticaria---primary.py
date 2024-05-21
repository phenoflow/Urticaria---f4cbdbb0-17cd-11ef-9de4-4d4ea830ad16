# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"M282000","system":"readv2"},{"code":"M28y100","system":"readv2"},{"code":"M280.00","system":"readv2"},{"code":"M28y.11","system":"readv2"},{"code":"M28z.00","system":"readv2"},{"code":"M284.00","system":"readv2"},{"code":"M281.00","system":"readv2"},{"code":"M285.00","system":"readv2"},{"code":"M287.00","system":"readv2"},{"code":"M280.11","system":"readv2"},{"code":"M286.00","system":"readv2"},{"code":"M28y000","system":"readv2"},{"code":"M28y200","system":"readv2"},{"code":"M282z00","system":"readv2"},{"code":"M282.00","system":"readv2"},{"code":"M282111","system":"readv2"},{"code":"M283.11","system":"readv2"},{"code":"2F8Z.00","system":"readv2"},{"code":"PH32100","system":"readv2"},{"code":"M283.00","system":"readv2"},{"code":"Myu4.00","system":"readv2"},{"code":"M12A200","system":"readv2"},{"code":"M28..00","system":"readv2"},{"code":"M282100","system":"readv2"},{"code":"51725.0","system":"readv2"},{"code":"20986.0","system":"readv2"},{"code":"43163.0","system":"readv2"},{"code":"11883.0","system":"readv2"},{"code":"15310.0","system":"readv2"},{"code":"49257.0","system":"readv2"},{"code":"45386.0","system":"readv2"},{"code":"1869.0","system":"readv2"},{"code":"7244.0","system":"readv2"},{"code":"70628.0","system":"readv2"},{"code":"1272.0","system":"readv2"},{"code":"6400.0","system":"readv2"},{"code":"17710.0","system":"readv2"},{"code":"38554.0","system":"readv2"},{"code":"50836.0","system":"readv2"},{"code":"9041.0","system":"readv2"},{"code":"8948.0","system":"readv2"},{"code":"1594.0","system":"readv2"},{"code":"65374.0","system":"readv2"},{"code":"15138.0","system":"readv2"},{"code":"23645.0","system":"readv2"},{"code":"39255.0","system":"readv2"},{"code":"7031.0","system":"readv2"},{"code":"1876.0","system":"readv2"},{"code":"6678.0","system":"readv2"},{"code":"20919.0","system":"readv2"},{"code":"7651.0","system":"readv2"},{"code":"24845.0","system":"readv2"},{"code":"16294.0","system":"readv2"},{"code":"30016.0","system":"readv2"},{"code":"L50","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('urticaria-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["urticaria---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["urticaria---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["urticaria---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
