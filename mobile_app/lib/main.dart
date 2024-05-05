import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Todo App',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: TodoListScreen(),
    );
  }
}

class TodoListScreen extends StatefulWidget {
  @override
  _TodoListScreenState createState() => _TodoListScreenState();
}

class _TodoListScreenState extends State<TodoListScreen> {
  List todos = [];
  final TextEditingController titleController = TextEditingController();
  final TextEditingController descriptionController = TextEditingController();

  @override
  void initState() {
    super.initState();
    fetchTodos();
  }

  void fetchTodos() async {
    final response = await http.get(Uri.parse('http://10.0.2.2:5000/api/todos')); // Adjust the IP address as per your setup
    if (response.statusCode == 200) {
      setState(() {
        todos = json.decode(response.body);
      });
    } else {
      throw Exception('Failed to load todos');
    }
  }

  void addTodo() async {
    final response = await http.post(
      Uri.parse('http://10.0.2.2:5000/api/todos'),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
      },
      body: json.encode({
        'title': titleController.text,
        'description': descriptionController.text,
      }),
    );
    if (response.statusCode == 201) {
      fetchTodos(); // Refresh the list after adding
      titleController.clear();
      descriptionController.clear();
    } else {
      throw Exception('Failed to add todo');
    }
  }

  void updateTodo(String id) async {
    final response = await http.put(
      Uri.parse('http://10.0.2.2:5000/api/todos/$id'),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
      },
      body: json.encode({
        'title': titleController.text,
        'description': descriptionController.text,
      }),
    );
    if (response.statusCode == 200) {
      fetchTodos(); // Refresh the list after updating
    } else {
      throw Exception('Failed to update todo');
    }
  }

  void deleteTodo(String id) async {
    final response = await http.delete(
      Uri.parse('http://10.0.2.2:5000/api/todos/$id'),
    );
    if (response.statusCode == 204) {
      fetchTodos(); // Refresh the list after deletion
    } else {
      throw Exception('Failed to delete todo');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('To-Do List'),
        actions: <Widget>[
          IconButton(
            icon: Icon(Icons.add),
            onPressed: () => showDialog(
              context: context,
              builder: (context) => AlertDialog(
                title: Text('Add New Todo'),
                content: Column(
                  children: <Widget>[
                    TextField(
                      controller: titleController,
                      decoration: InputDecoration(hintText: 'Title'),
                    ),
                    TextField(
                      controller: descriptionController,
                      decoration: InputDecoration(hintText: 'Description'),
                    ),
                  ],
                  mainAxisSize: MainAxisSize.min,
                ),
                actions: <Widget>[
                  TextButton(
                    child: Text('Cancel'),
                    onPressed: () => Navigator.of(context).pop(),
                  ),
                  TextButton(
                    child: Text('Add'),
                    onPressed: () {
                      addTodo();
                      Navigator.of(context).pop();
                    },
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
      body: ListView.builder(
        itemCount: todos.length,
        itemBuilder: (context, index) {
          var todo = todos[index];
          return ListTile(
            title: Text(todo['title']),
            subtitle: Text(todo['description']),
            trailing: IconButton(
              icon: Icon(Icons.delete),
              onPressed: () => deleteTodo(todo['id']),
            ),
            onTap: () => showDialog(
              context: context,
              builder: (context) => AlertDialog(
                title: Text('Edit Todo'),
                content: Column(
                  children: <Widget>[
                    TextField(
                      controller: titleController..text = todo['title'],
                      decoration: InputDecoration(hintText: 'Title'),
                    ),
                    TextField(
                      controller: descriptionController..text = todo['description'],
                      decoration: InputDecoration(hintText: 'Description'),
                    ),
                  ],
                  mainAxisSize: MainAxisSize.min,
                ),
                actions: <Widget>[
                  TextButton(
                    child: Text('Cancel'),
                    onPressed: () => Navigator.of(context).pop(),
                  ),
                  TextButton(
                    child: Text('Update'),
                    onPressed: () {
                      updateTodo(todo['id']);
                      Navigator.of(context).pop();
                    },
                  ),
                ],
              ),
            ),
          );
        },
      ),
    );
  }
}
