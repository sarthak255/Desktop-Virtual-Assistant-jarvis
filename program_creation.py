# src/program_creation.py

import os

# Function to create a basic program structure
def create_program(platform, language, project_name):
    base_dir = f"./{project_name}"
    
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    
    if platform.lower() == "android":
        create_android_project(base_dir, language)
    elif platform.lower() == "windows":
        create_windows_project(base_dir, language)
    elif platform.lower() == "linux":
        create_linux_project(base_dir, language)
    elif platform.lower() == "mac":
        create_mac_project(base_dir, language)
    else:
        print("Unsupported platform.")
        return

    print(f"{language.capitalize()} project for {platform.capitalize()} created at {base_dir}.")

def create_android_project(base_dir, language):
    if language.lower() == "java":
        src_dir = os.path.join(base_dir, "app/src/main/java/com/example")
        os.makedirs(src_dir)
        main_activity = """package com.example;

import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
}
"""
        with open(os.path.join(src_dir, "MainActivity.java"), "w") as f:
            f.write(main_activity)
    elif language.lower() == "kotlin":
        src_dir = os.path.join(base_dir, "app/src/main/java/com/example")
        os.makedirs(src_dir)
        main_activity = """package com.example

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }
}
"""
        with open(os.path.join(src_dir, "MainActivity.kt"), "w") as f:
            f.write(main_activity)
    # Add more languages as needed

def create_windows_project(base_dir, language):
    if language.lower() == "csharp":
        src_dir = os.path.join(base_dir, "src")
        os.makedirs(src_dir)
        main_program = """using System;

namespace HelloWorld
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
        }
    }
}
"""
        with open(os.path.join(src_dir, "Program.cs"), "w") as f:
            f.write(main_program)
    # Add more languages as needed

def create_linux_project(base_dir, language):
    if language.lower() == "c":
        src_dir = os.path.join(base_dir, "src")
        os.makedirs(src_dir)
        main_program = """#include <stdio.h>

int main() {
    printf("Hello, World!\\n");
    return 0;
}
"""
        with open(os.path.join(src_dir, "main.c"), "w") as f:
            f.write(main_program)
    elif language.lower() == "python":
        src_dir = os.path.join(base_dir, "src")
        os.makedirs(src_dir)
        main_program = """print("Hello, World!")"""
        with open(os.path.join(src_dir, "main.py"), "w") as f:
            f.write(main_program)
    # Add more languages as needed

def create_mac_project(base_dir, language):
    if language.lower() == "swift":
        src_dir = os.path.join(base_dir, "src")
        os.makedirs(src_dir)
        main_program = """import Cocoa

@NSApplicationMain
class AppDelegate: NSObject, NSApplicationDelegate {

    func applicationDidFinishLaunching(_ aNotification: Notification) {
        // Insert code here to initialize your application
    }

    func applicationWillTerminate(_ aNotification: Notification) {
        // Insert code here to tear down your application
    }
}
"""
        with open(os.path.join(src_dir, "AppDelegate.swift"), "w") as f:
            f.write(main_program)
    # Add more languages as needed

# Test the program creation functions
if __name__ == "__main__":
    create_program("android", "java", "AndroidJavaProject")
    create_program("windows", "csharp", "WindowsCSharpProject")
    create_program("linux", "python", "LinuxPythonProject")
    create_program("mac", "swift", "MacSwiftProject")
