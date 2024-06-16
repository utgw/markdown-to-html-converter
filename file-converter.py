import markdown as md
import sys

def markdown(inputfile, outputfile):
  contents = ''
  with open(inputfile) as f:
    contents = f.read()
  with open(outputfile, 'w') as f:
    html = md.markdown(contents)
    f.write(html)
    
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 file-converter.py markdown <inputfile> <outputfile>")
        sys.exit(1)
    _, func_name, input_file, output_file = sys.argv

    if func_name == 'markdown':
      markdown(input_file, output_file)
    else:
      print(f"Unknown fuction: {func_name}")
      exit(1)