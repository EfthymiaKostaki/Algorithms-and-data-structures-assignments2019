import sys, argparse, json, math

#The purpose of the canvas method was to identify each square with the only unique characteristic we can calculate 
#which is the center of the square. 
#We examine different situations for the lines using the sum of their angles in order to determine the sequence of the squares.
#This function doesn't work properly and never breaks out of the while
def canvas(total, lines, angles):
    middle_points = list()
    step_length = 1.0 #We know that each time step length is going to be 1.
    rule = list()
    count = 0
    angles_sum = angles[count]
    total_sqrt = float(math.sqrt(total))
    choice = list()

    while count != total:
        print(middle_points, rule)
        stuck = False
        unique_choice = False

        #When we don't have unique choice we will start to look from Left side
        if angles_sum == 0.0 or angles_sum == -0.0 or angles_sum == 90.0:
            if lines[count][1] == lines[count][3] == 0.0:
                unique_choice = True
                check_point = [lines[count][0] + step_length / 2, lines[count][1] + step_length / 2]
                if check_point not in middle_points:
                    middle_points.append(check_point)
                    rule.append("L")
                    count += 1
                    angles_sum += angles[count]
                else:
                    stuck = True
            elif lines[count][0] == lines[count][2] == 0.0:
                unique_choice = True
                check_point = [lines[count][0] + step_length / 2, lines[count][1] + step_length / 2]
                if check_point not in middle_points:
                    middle_points.append(check_point)
                    rule.append("R")
                    count += 1
                    angles_sum += angles[count]
                else:
                    stuck = True
            elif lines[count][1] == lines[count][3] == total_sqrt:
                unique_choice = True
                check_point = [lines[count][0] + step_length / 2, lines[count][1] - step_length / 2]
                if check_point not in middle_points:
                    middle_points.append(check_point)
                    rule.append("R")
                    count += 1
                    angles_sum += angles[count]
                else:
                    stuck = True
            elif lines[count][0] == lines[count][2] == total_sqrt:
                unique_choice = True
                check_point = [lines[count][0] - step_length / 2, lines[count][1] + step_length / 2]
                if check_point not in middle_points:
                    middle_points.append(check_point)
                    rule.append("L")
                    count += 1
                    angles_sum += angles[count]
                else:
                    stuck = True
            if not unique_choice and not(len(choice) > 0 and choice[-1] == count):
                if lines[count][0] == lines[count][2]:
                    check_point = [lines[count][0] - step_length / 2, lines[count][1] + step_length / 2]
                    if check_point not in middle_points:
                        rule.append("L")
                        middle_points.append(check_point)
                    else:
                        stuck = True
                else:
                    check_point = [lines[count][0] + step_length / 2, lines[count][1] + step_length / 2]
                    if check_point not in middle_points:
                        middle_points.append(check_point)
                        rule.append("L")
                    else:
                        stuck = True
                if not stuck:
                    choice.append(count)
                    count += 1
                    angles_sum += angles[count]
            if (not unique_choice and stuck) or (len(choice) > 0 and choice[-1] == count):
                stuck = False
                if lines[count][0] == lines[count][2]:
                    check_point = [lines[count][0] + step_length / 2, lines[count][1] + step_length / 2]
                    if check_point not in middle_points:
                        middle_points.append(check_point)
                        rule.append("R")
                    else:
                        stuck = True
                else:
                    check_point = [lines[count][0] - step_length / 2, lines[count][1] - step_length / 2]
                    if check_point not in middle_points:
                        middle_points.append(check_point)
                        rule.append("R")
                    else:
                        stuck = True
                if (len(choice) > 0 and choice[-1] == count):
                    choice.pop()
                if not stuck:
                    count += 1
                    angles_sum += angles[count]
        else:#meaning we are in the opposite direction
            if lines[count][1] == lines[count][3] == 0.0:
                unique_choice = True
                check_point = [lines[count][0] - step_length / 2, lines[count][1] + step_length / 2]
                if check_point not in middle_points:
                    middle_points.append(check_point)
                    rule.append("R")
                    count += 1
                    angles_sum += angles[count]
                else:
                    stuck = True
            elif lines[count][0] == lines[count][2] == 0.0:
                unique_choice = True
                check_point = [lines[count][0] + step_length / 2, lines[count][1] - step_length / 2]
                if check_point not in middle_points:
                    middle_points.append(check_point)
                    rule.append("L")
                    count += 1
                    angles_sum += angles[count]
                else:
                    stuck = True
            elif lines[count][0] == lines[count][2] == total_sqrt:
                unique_choice = True
                check_point = [lines[count][0] - step_length / 2, lines[count][1] - step_length / 2]
                if check_point not in middle_points:
                    middle_points.append(check_point)
                    rule.append("R")
                    count += 1
                    angles_sum += angles[count]
                else:
                    stuck = True
            elif lines[count][1] == lines[count][3] == total_sqrt:
                unique_choice = True
                check_point = [lines[count][0] - step_length / 2, lines[count][1] - step_length / 2]
                if check_point not in middle_points:
                    middle_points.append(check_point)
                    rule.append("L")
                    count += 1
                    angles_sum += angles[count]
                else:
                    stuck = True
            if not unique_choice and  not(len(choice) > 0 and choice[-1] == count):
                if lines[count][0] == lines[count][2]:
                    check_point = [lines[count][0] + step_length / 2, lines[count][1] - step_length / 2]
                    if check_point not in middle_points:
                        middle_points.append(check_point)
                    else:
                        stuck = True
                else:
                    check_point = [lines[count][0] - step_length / 2, lines[count][1] - step_length / 2]
                    if check_point not in middle_points:
                        middle_points.append(check_point)
                    else:
                        stuck = True
                if not stuck:
                    count += 1
                    angles_sum += angles[count]
            if (not unique_choice and stuck) or (len(choice) > 0 and choice[-1] == count):
                stuck = False
                if lines[count][0] == lines[count][2]:
                    check_point = [lines[count][0] - step_length / 2, lines[count][1] - step_length / 2]
                    if check_point not in middle_points:
                        middle_points.append(check_point)
                    else:
                        stuck = True
                else:
                    check_point = [lines[count][0] + step_length / 2, lines[count][1] + step_length / 2]
                    if check_point not in middle_points:
                        middle_points.append(check_point)
                    else:
                        stuck = True
                if (len(choice) > 0 and choice[-1] == count):
                    choice.pop()
                if not stuck:
                    count += 1
                    angles_sum += angles[count]
        if stuck:
            middle_points.pop()
            rule.pop()
            angles_sum -= angles[count]
            count -= 1
    return rule

                

def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-d", "--derive", action="store_true", default= False)
    group.add_argument("-m", "--message", action="store_true", default= False)

    parser.add_argument("json_file", help="import the json file ",   nargs='?')
    parser.add_argument("output_file", help="export the txt file with positions",  nargs='?')

    args = parser.parse_args()
    export_output_file = True
    import_canvas_file = False
    input_file = sys.argv[1]

    if args.message:
        input_file = sys.argv[2]
        export_output_file = False
    elif args.derive:
        input_file = sys.argv[2]
        export_output_file = False
        import_canvas_file = True

    if import_canvas_file:
        list_line = list()
        angles = list()
        i = 0
        with open(input_file, "r") as f:
            for i, l in enumerate(f):
                l = l.replace("(", "").replace(")", "").replace(",","")
                list_line.append([float(x) for x in l.split()])
                
        for k, key in enumerate(list_line):
            for j in range(0,4):
                list_line[k][j] =  list_line[k][j] / math.sqrt(i + 1) 
                if k != 0:
                    x1, y1 = list_line[k - 1][2] - list_line[k - 1][0], list_line[k - 1][3] - list_line[k - 1][1]
                    x2, y2 = list_line[k][2] - list_line[k][0], list_line[k][3] - list_line[k][1]
                    angles.append(math.degrees(math.atan2(x1*y2-y1*x2,x1*x2+y1*y2)))
        #We will create a list containing the middle points of the squares and then we will return the rule as a list
        f_rule = canvas(i + 1, 0, list(), list_line, angles, 0.0)
        g_rule = canvas(i + 1, 0, list(), list_line[:-1], angles,  math.fsum(angles))

        #Then we have to add in each string the correct corners
        print("F -> ", f_rule, "\nG -> ", g_rule)
                
    else:
            with open(input_file, "r") as f:
                json_dict = json.load(f)
            axiom = list(json_dict["axiom"])
            keys = json_dict["rules"].keys()

            for i in range(json_dict["order"]):
                for index, value in enumerate(axiom):
                    if value in keys:
                        axiom[index] = json_dict["rules"][value]
                axiom =list(map(lambda x: list(x), axiom))
                flat_list = []
                for sublist in axiom:
                    for item in sublist:
                        flat_list.append(item)
                axiom =  flat_list
            string_axiom = "".join(axiom)
            if not export_output_file:
                print(string_axiom)
            else:
                f = open(sys.argv[2], "w")
                angle = json_dict["start_angle"]
                current_position_x = 0
                current_position_y = 0
                step_length = json_dict["step_length"]
                remember = []

                for i in axiom:
                    if i == "+":
                        angle = angle + json_dict["left_angle"]
                    elif i == "-":
                        angle = angle - json_dict["right_angle"]
                    elif i == "[":
                        remember.append([current_position_x, current_position_y, angle])
                    elif i == "]":
                        current_position_x, current_position_y, angle = remember.pop()
                    elif i in ['A', 'B','C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']:
                        f.write("({}, {}) ".format(current_position_x, current_position_y))
                        current_position_x = round(current_position_x + math.cos(math.radians(angle)) * step_length, 2)
                        current_position_y = round(current_position_y + math.sin(math.radians(angle)) * step_length, 2)
                        f.write("({}, {}) \n".format(current_position_x, current_position_y))

              

if __name__ == '__main__':
    main()
