def arithmetic_arranger(problems,calculate=False):
  arranged_problems =""
  operators = ["+", "-"]
  top_row, middle_row, lines, bottom_row = "","","",""
  space = 4 * " "


  if len(problems) > 5:
    return "Error: Too many problems."

  for index, problem in enumerate(problems):
    elements = problem.split(" ")
    first_element = elements[0]
    operator = elements[1]
    second_element = elements[2]

    if not first_element.isdigit() or not second_element.isdigit():
      return "Error: Numbers must only contain digits."
    if operator not in operators:
      return "Error: Operator must be '+' or '-'."
    if len(first_element) > 4 or len(second_element) > 4:
      return "Error: Numbers cannot be more than four digits." 

    length = get_max_length(first_element,second_element)
    
    top_row += str(first_element.rjust(length))
    middle_row += str(operator + second_element.rjust(length-1))
    lines += '-' * length
    bottom_row += str(get_result(operator,first_element,second_element)).rjust(length)

    if index < len(problems):
      top_row += space
      middle_row += space
      lines += space
      bottom_row += space

    if calculate == True:
      arranged_problems = top_row.rstrip() + "\n" + middle_row.rstrip() + "\n" + lines.rstrip() + "\n" + bottom_row.rstrip()
    else:
      arranged_problems = top_row.rstrip() + "\n" + middle_row.rstrip() + "\n" + lines.rstrip()

  return arranged_problems

def get_max_length(first_element, second_element):
  max_length = max(len(first_element),len(second_element)) + 2
  return max_length
   
def get_result(operator,first_element,second_element):
  addition = int(first_element) + int(second_element)
  subtraction = int(first_element) - int(second_element)
  operators = {"+":addition,"-":subtraction}
  return operators.get(operator)
  