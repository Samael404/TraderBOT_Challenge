var mysql       = require('mysql');
var connection = mysql.createConnection({
    host        : 'localhost',
    user        : 'root',
    password    : 'password',
    database    : 'traderbot_challenge'
});

connection.connect(function(err){
    if(!err) {
        console.log("Database is connected ... nn");
    } else {
        console.log("Error connecting database ... nn");
    }
});

exports.register = function(req,res){
    var today = new Date();
    bcrypt.hash(req.body.password, 5, function( err, bcryptedPassword){

    var users ={
        "username":req.body.username,
        "password":req.body.password,
        "created":today,
        "modified":today
    }
    connection.query('INSERT INTO users SET ?',users, function (error, results, fields){
    if (error) {
        console.log("error occurred",error);
        res.send({
            "code":400,
            "failed":"error occurred"
        })
    } else{
        console.log('The solution is: ', results);
        res.send({
            "code":200,
            "success":"user registered sucessfully"
        });
    }
exports.login = function(req,res){
    var username= req.body.username;
    var password = req.body.password;
    connection.query("SELECT * FROM users WHERE username = ?",[username], function (error, results, fields){
    if (error) {
        //console.log("error occured",error);
        res.send({
            "code":400,
            "failed":"error occured"
        })
    } else{
        //console.log('The solution is: ', results);
        if(results.length >0){
            bcrypt.compare(password, results[0].password, function(err, doesMatch){
                if (doesMatch){
                res.send({
                    "code":200,
                    "success":"login successful"
                });
        }else{
            res.send({
                "code":204,
                "success":"Username and password does not match"
            });
        }
    });    
}
        else{
        res.send({
            "code":204,
            "success":"Username does not exist"
        });
    }        
    }
});