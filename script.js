
    ctx.arc(centerX, centerY, radius, currentAngle, currentAngle + arcSize);
    ctx.lineTo(centerX, centerY);
    ctx.fill();
    ctx.strokeStyle = "#fff";
    ctx.stroke();
    ctx.closePath();

    ctx.save();
    ctx.translate(centerX, centerY);
    ctx.rotate(currentAngle + arcSize / 2);
    ctx.textAlign = "right";
    ctx.fillStyle = "#000";
    ctx.font = "18px Arial";
    ctx.fillText(genre, radius - 10, 5);
    ctx.restore();

    currentAngle += arcSize;
  });
}
