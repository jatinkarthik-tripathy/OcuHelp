import 'resultPage.dart';
import 'package:flutter/material.dart';
import 'dart:io';
import 'package:image_picker/image_picker.dart';
import 'api.dart';
import 'package:toast/toast.dart';

class Home extends StatefulWidget {
  @override
  State<StatefulWidget> createState() => HomeState();
}

class HomeState extends State<Home> {
  File _image;

  Future getImage(bool isCamera) async {
    File image;

    if (isCamera) {
      image = await ImagePicker.pickImage(source: ImageSource.camera);
    } else {
      image = await ImagePicker.pickImage(source: ImageSource.gallery);
    }
    uploadImage(image, uploadUrl);
    Toast.show("IMAGE UPLOADED !", context,
        duration: Toast.LENGTH_LONG,
        textColor: Colors.black,
        backgroundColor: Colors.white12,
        backgroundRadius: 15,
        gravity: Toast.BOTTOM);

    setState(() {
      _image = image;
    });
  }

  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: Container(
        color: Colors.white,
        child: Scaffold(
          backgroundColor: Colors.transparent,
          appBar: AppBar(
            backgroundColor: Colors.transparent,
            centerTitle: true,
            elevation: 0,
            title: Text(
              'OcuHelp',
              style: TextStyle(
                  fontSize: 40,
                  fontWeight: FontWeight.bold,
                  color: Colors.black),
            ),
          ),
          body: Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                Container(
                  color: Colors.blue,
                  child: IconButton(
                    icon: Icon(Icons.insert_drive_file),
                    color: Colors.white,
                    iconSize: 70,
                    onPressed: () {
                      getImage(false);
                    },
                  ),
                ),
                SizedBox(
                  height: 70.0,
                ),
                Container(
                  color: Colors.blue,
                  child: IconButton(
                    icon: Icon(Icons.camera_alt),
                    color: Colors.white,
                    iconSize: 70,
                    onPressed: () {
                      getImage(true);
                    },
                  ),
                ),
                SizedBox(
                  height: 70.0,
                ),
              ],
            ),
          ),
          floatingActionButton: FloatingActionButton.extended(
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => ResultPage(
                    image: _image,
                  ),
                ),
              );
            },
            icon: Icon(
              Icons.arrow_forward,
              color: Colors.white,
              size: 30,
            ),
            label: Text(
              "Next",
              style: TextStyle(color: Colors.white, fontSize: 20),
            ),
            backgroundColor: Colors.blue,
          ),
        ),
      ),
    );
  }
}
