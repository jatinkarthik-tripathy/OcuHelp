import 'dart:io';
import 'package:flutter/material.dart';
import 'package:flutter_tts/flutter_tts.dart';
import 'api.dart';

class ResultPage extends StatefulWidget {
  final File image;
  ResultPage({@required this.image});

  @override
  State<StatefulWidget> createState() => ResultPageState(image);
}

class ResultPageState extends State<ResultPage> {
  String captions = "Refresh once !";
  var data;
  File image;
  FlutterTts ftts = FlutterTts();

  ResultPageState(this.image);

  Widget build(BuildContext context) {
    return Container(
      color: Colors.white,
      child: Scaffold(
        backgroundColor: Colors.transparent,
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              Container(
                //color: Colors.white,
                //margin: EdgeInsets.all(5),
                padding: EdgeInsets.all(10),
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(20),
                  color: Colors.white,
                ),
                child: Text(
                  "Captions",
                  style: TextStyle(
                      fontSize: 40,
                      fontWeight: FontWeight.bold,
                      color: Colors.black),
                ),
              ),
              SizedBox(
                height: 30,
              ),
              Container(
                decoration: BoxDecoration(
                  border: Border.all(color: Colors.white, width: 3),
                ),
                child: displayImage(image),
              ),
              SizedBox(
                height: 20,
              ),
              Container(
                height: 100,
                width: 200,
                padding: EdgeInsets.all(5),
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(10),
                  color: Colors.white,
                ),
                child: Text(
                  captions,
                  style: TextStyle(color: Colors.black),
                ),
              ),
              SizedBox(
                height: 20,
              ),
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[
                  ElevatedButton(
                    child: Text(
                      "Refresh",
                      style: TextStyle(
                        color: Colors.black,
                      ),
                    ),
                    onPressed: () => getCaption(),
                  ),
                  SizedBox(
                    width: 25,
                  ),
                  ElevatedButton(
                    child: Text(
                      "Audio",
                      style: TextStyle(
                        color: Colors.black,
                      ),
                    ),
                    onPressed: () => speakCaption(),
                  ),
                ],
              )
            ],
          ),
        ),
        /*
      floatingActionButton: FloatingActionButton.extended(
                onPressed: () => Navigator.pushNamed(context, "/"),
                icon: Icon(
                Icons.arrow_back,color: Colors.black,size: 30,
                ),
                label: Text("Back",style: TextStyle(color: Colors.black),),
                ),
      */
      ),
    );
  }

  Future getCaption() async {
    data = await getData(uploadUrl);

    setState(() {
      captions = data['captions'];
    });
  }

  speakCaption() async {
    await ftts.setLanguage("en-UK");
    await ftts.setPitch(2);
    await ftts.speak(captions);
  }

  Widget displayImage(File file) {
    return new SizedBox(
      height: 250.0,
      width: 200.0,
      child: Image.file(file),
    );
  }
}
