package main

import (
	"bytes"
	"encoding/base64"
	"image"
	"image/color"
	"image/draw"
	"image/png"
	"log"
	"math"
	"os"
)

type Canvas struct {
	image.RGBA
}

func NewCanvas(r image.Rectangle) *Canvas {
	canvas := new(Canvas)
	canvas.RGBA = 
}
