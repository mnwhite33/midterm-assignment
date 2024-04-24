const express = require('express')
const app = express()

const bodyParser = require('body-parser')
require('dotenv/config')
app.use(bodyParser.json())

const mongoose = require('mongoose')

const postsRoute = require('./routes/posts')
const authRoute= require('./routes/auth')

app.use('/post',postsRoute)
app.use('/user',authRoute)


app.get('/', (req,res)=>{
    res.send('Homepage')
})

// const MURL = 'mongodb+srv://stelios:1234@cluster0.rkfq3.mongodb.net/MiniFilms?retryWrites=true&w=majority'
const MURL = process.env.DB_CONNECTOR
mongoose.connect(MURL).then(() => { console.log('Your mongoDB connector is on...')})


app.listen(3000, ()=>{
    console.log('Your server is up and running...')
})
