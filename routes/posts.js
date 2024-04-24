const express = require('express')
const router = express.Router()

const Post = require('../models/Post')
const verifyToken = require('../verifyToken')

router.get('/', verifyToken, async(req,res) =>{
    try{
        const posts = await Post.find()
        res.send(posts)
    }catch(err){
        res.status(400).send({message:err})
    }
})

// router.get('/', async (req,res) =>{ 
//     try{
//         const posts = await Post.find() 
//         res.send(posts)
//     }catch(err){
//         res.send({message:err})
//     }
// })

// GET 2 (Read by ID)
router.get('/:postId', verifyToken,async(req,res) =>{
    console.log(req.params.postId)
    const getPostById = await Post.findById(req.params.postId)
    res.send(getPostById)
})

// POST (Create data)
router.post('/',verifyToken,async(req,res)=>{
    console.log(req.body)

    const postData = new Post({
        title:req.body.title,
        topic:req.body.topic,
        timestamp:req.body.timestamp,
        message:req.body.message
    })
    // try to insert...
    try{
        const postToSave = await postData.save()
        res.send(postToSave)
    }catch(err){
        res.send({message:err})
    }
})

// PATCH (Update)
router.patch('/:postId', verifyToken, async(req,res) =>{
    try{
        const updatePostById = await Post.updateOne(
            {_id:req.params.postId},
            {$set:{
                title:req.body.title,
                topic:req.body.topic,
                timestamp:req.body.timestamp,
                message:req.body.message
                }
            })
        res.send(updatePostById)
    }catch(err){
        res.send({message:err})
    }
})

// DELETE (Delete)
router.delete('/:postId?',verifyToken,async(req,res)=>{
    try{
        // const deletePostById = await Post.deleteOne({_id:req.params.postId})
        // res.send(deletePostById)
        if (req.params.postId) {
            // If postId is provided, delete the specific post
            const deletePostById = await Post.deleteOne({ _id: req.params.postId });
            res.send(deletePostById);
        } else {
            // If no postId is provided, delete all posts
            const deleteAllPosts = await Post.deleteMany({});
            res.send(deleteAllPosts); }
    }catch(err){
        res.send({message:err})
    }
})

module.exports = router
