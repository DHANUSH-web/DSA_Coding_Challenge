using System;
using System.IO;
using System.Collections.Generic;

class Files
{
    public static string ReadFile(string filename)      // static method return the file content
    {
        try
        {
            string file_content = File.ReadAllText(filename);
            return file_content;
        }

        catch (FileNotFoundException fe)
        {
            throw fe;
        }
    }

    public static void WriteFile(string filename, string content)   // static method to create a new file
    {
        File.WriteAllText(filename, content);
    }

    public static void AppendText(string filename, string content)   // static method to append content to existing file
    {
        try
        {
            File.AppendAllText(filename, content);
        }
        catch (Exception e)
        {
            throw e;
        }
    }

    public static string GetExtension(string filename)     // static method to return the extension of a file
    {
        string[] file_split = filename.Split(".");

        return file_split[file_split.Length - 1];
    }

    public static string GetBaseName(string file_path)  // static method to return base name of abs path
    {
        string[] base_name;
        if (file_path.Contains("/"))
        {
            base_name = file_path.Split("/");
        }

        else if (file_path.Contains("//"))
        {
            base_name = file_path.Split("//");
        }

        else
        {
            base_name = file_path.Split("\\");
        }

        return base_name[base_name.Length - 1];
    }

    public static string GetFileBaseName(string filename)   // static method to return the base name of a file
    {
        string[] f_base = GetBaseName(filename).Split(".");

        return f_base[0];
    }

    public static string GetFileType(string filename)   // static method to return the file type of a file
    {
        Dictionary<string, string> file_types = new Dictionary<string, string>{
            {"py", "Python File"},
            {"c", "C source file"},
            {"cs", "C# source file"},
            {"cpp", "C++ source file"},
            {"html", "Hyper Text Markup Language file"},
            {"css", "Cascade Style Sheet"},
            {"java", "Java program file"},
            {"js", "Java Script file"},
            {"rb", "Ruby File"},
            {"dkr", "Docker"},
            {"go", "GO file"},
            {"php", "PHP file"},
            {"zip", "ZIP file"},
            {"rar", "RAR file"},
            {"doc", "MS document file"},
            {"pyw", "Python On work file"},
            {"v", "Verilog File"},
            {"tb", "Verilog test bench"},
            {"txt", "Text File"},
            {"bat", "Batch File"},
            {"sh", "Linux installer"},
            {"exe", "Windows Executable File"},
            {"o", "gcc compiled output file"}
        };

        string ext = GetExtension(filename);

        if (file_types.ContainsKey(ext))
        {
            return file_types[ext];
        }

        return "Unknown";
    }

    public static int GetFileSize(string filename)  // static method to return the actual file size of a file
    {
        if (File.Exists(filename))
        {
            return ReadFile(filename).Length;
        }

        return -1;
    }

    public static string GetFileSizeStr(string filename)    // static method to return the formatted size
    {
        try
        {
            int sz = GetFileSize(filename);
            string str_sz;

            if (sz < 1000) str_sz = $"{sz} B";
            else if (sz >= 1000 && sz < 1e6) str_sz = $"{ToDecimalPoint(sz/1e3)} KB";
            else if (sz >= 1e6 && sz < 1e9) str_sz = $"{ToDecimalPoint(sz/1e6)} MB";
            else str_sz = $"{ToDecimalPoint(sz/1e9)} GB";

            return str_sz;
        }
        catch (FileNotFoundException e)
        {
            return e.Message;
        }
    }

    public static string GetAbsFilePath(string filename)    // static method to return the abs file path of a file
    {
        return Path.GetFullPath(filename);
    }

    public static string GetFileCTD(string filename)    // static method to return creation time of a file
    {
        if (File.Exists(filename))
            return File.GetCreationTime(filename).ToString();

        return "NULL";
    }

    public static string GetDeveloper()     // method returns the developer of this package/namespace
    {
        return "Dhanush H V";
    }

    public static int CountLines(string filename)   // method to return number of lines of a file
    {
        if (File.Exists(filename))
        {
            string[] lines = File.ReadAllLines(filename);
            return lines.Length;
        }

        return 1;
    }

    public static double ToDecimalPoint(double num, int dec=2)  // method to return the double value to specific dec-point
    {
        string org_num = num.ToString();
        string[] fnd_pnt = org_num.Split(".");


        if (fnd_pnt.Length == 2 && fnd_pnt[1].Length > 2 && dec <= fnd_pnt[1].Length)
        {
            string pnt = fnd_pnt[0] + ".";

            for (int i = 0; i < dec; i++)
            {
                pnt += fnd_pnt[1][i];
            }

            return Convert.ToDouble(pnt);
        }
        
        return num;
    }

    public static float ToDecimalPoint(float num, int dec=2)    // same method applied for float
    {
        string org_num = num.ToString();
        string[] fnd_pnt = org_num.Split(".");


        if (fnd_pnt.Length == 2 && fnd_pnt[1].Length > 2 && dec <= fnd_pnt[1].Length)
        {
            string pnt = fnd_pnt[0] + ".";

            for (int i = 0; i < dec; i++)
            {
                pnt += fnd_pnt[1][i];
            }

            return float.Parse(pnt);
        }
        
        return num;
    }
}

namespace HelloWorld
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            // string file = @"/home/dhanush/Documents/c#/HelloWorld/Program.cs";
            string file = "testFile.txt";

            Console.WriteLine(Files.GetFileType(file));
        }
    }
}