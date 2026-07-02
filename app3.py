for (let i = enemies.length - 1; i >= 0; i--) {
            let enemy = enemies[i];
            let distToPlayer = player.x - enemy.x;
            enemy.faceDir = distToPlayer > 0 ? 1 : -1;
            enemy.vx = Math.sign(distToPlayer) * 1.8;
            
            if (player.attacking && Math.abs(player.x - enemy.x) < 55) {
                enemy.hp -= 2; player.attacking = false;
            }
            allies.forEach(ally => {
                if (ally.attacking && Math.abs(ally.x - enemy.x) < 55) { enemy.hp -= 1; }
            });

            updatePhysics(enemy);
            drawAdvancedSkin(enemy.x, enemy.y, enemy.type, false, enemy.faceDir, enemy.color);
            drawHealthBar(enemy, 15);

            if (enemy.hp <= 0) { enemies.splice(i, 1); }
        }

        document.getElementById("enemyCount").innerText = enemies.length;

        if (enemies.length === 0 && !gameOver) {
            if (stage === 1) {
                stage = 2;
                document.getElementById("stage").innerText = "2 (موجة موبات عناكب ماين كرافت الضخمة)";
                spawnEnemies();
            } else {
                ctx.fillStyle = "#00ff88"; ctx.font = "bold 28px sans-serif";
                ctx.shadowBlur = 10; ctx.shadowColor = "#00ff88";
                ctx.fillText("🎉 كفو! انتصر فريقك وتم تطهير كل الخرائط بنجاح! 🎉", 80, 170);
                gameOver = true;
            }
        }

        if (!gameOver) requestAnimationFrame(loop);
    }

    spawnEnemies();
    loop();
</script>
</body>
</html>
"""

components.html(game_source_code, height=440)
st.markdown("---")
st.markdown("<p style='text-align: center; color: #8892b0;'>أداة التصميم التلقائي المدمجة بنظام عميل LEX 2099 - جاهزة للتشغيل الفوري</p>", unsafe_allow_html=True)
