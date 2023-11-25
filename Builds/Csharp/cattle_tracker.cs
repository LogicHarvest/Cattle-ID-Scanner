using System;
using System.Diagnostics;
using System.Windows.Forms;

public class MyForm : Form
{
    public MyForm()
    {
        // Create a button
        Button runButton = new Button();
        runButton.Text = "Run app.py";
        runButton.Click += RunButton_Click;

        // Add the button to the form
        Controls.Add(runButton);
    }

    private void RunButton_Click(object sender, EventArgs e)
    {
        // Path to your Python executable
        string pythonPath = @"C:\Path\To\Your\Python\python.exe";

        // Path to your app.py script
        string scriptPath = @"C:\Path\To\Your\app.py";

        // Create a process to run the Python script
        Process process = new Process();
        ProcessStartInfo startInfo = new ProcessStartInfo
        {
            FileName = pythonPath,
            Arguments = scriptPath,
            RedirectStandardOutput = true,
            UseShellExecute = false,
            CreateNoWindow = true
        };

        process.StartInfo = startInfo;

        // Start the process
        process.Start();

        // Optionally, you can read the output of the Python script
        string output = process.StandardOutput.ReadToEnd();

        // Wait for the process to exit
        process.WaitForExit();

        // Display a message (optional)
        MessageBox.Show("Python script executed. Output:\n" + output);
    }

    public static void Main()
    {
        Application.Run(new MyForm());
    }
}