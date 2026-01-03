# 📅 <% tp.date.now("YYYY-MM-DD") %> の振り返り

## 🔄 前日からの引き継ぎタスク
<%*
// 前日の日付を計算
const yesterday = moment(tp.date.now("YYYY-MM-DD")).subtract(1, 'days').format('YYYY-MM-DD');
const yesterdayFile = tp.file.find_tfile(yesterday);

if (yesterdayFile) {
    const content = await app.vault.read(yesterdayFile);
    // 未完了のタスク（- [ ] で始まる行）を抽出
    const lines = content.split('\n');
    const incompleteTasks = [];
    let inTaskSection = false;
    let taskIndent = 0;
    
    for (let i = 0; i < lines.length; i++) {
        const line = lines[i];
        const trimmed = line.trim();
        
        // タスクセクションの開始を検出
        if (trimmed.includes('## タスク') || trimmed.includes('## 🔄 前日からの引き継ぎタスク')) {
            inTaskSection = true;
            continue;
        }
        
        // 次のセクションが来たら終了
        if (inTaskSection && trimmed.startsWith('## ')) {
            break;
        }
        
        // タスク行を検出
        if (inTaskSection && (trimmed.startsWith('- [ ]') || trimmed.startsWith('- [x]'))) {
            // 完了済みタスクは未完了に戻す
            const taskText = line.replace(/^- \[x\]/, '- [ ]');
            incompleteTasks.push(taskText);
        } else if (inTaskSection && trimmed.startsWith('- [ ]') || trimmed.startsWith('- [x]')) {
            // インデントされたタスクも含める
            const taskText = line.replace(/^- \[x\]/, '- [ ]');
            incompleteTasks.push(taskText);
        } else if (inTaskSection && (line.match(/^\s+- \[ \]/) || line.match(/^\s+- \[x\]/))) {
            // インデントされたタスク（タブやスペース）
            const taskText = line.replace(/\[x\]/, '[ ]');
            incompleteTasks.push(taskText);
        }
    }
    
    if (incompleteTasks.length > 0) {
        tR += `<!-- 前日の日記: [[${yesterday}]] から引き継ぎ -->\n`;
        incompleteTasks.forEach(task => {
            tR += task + '\n';
        });
    } else {
        tR += `<!-- 前日の日記: [[${yesterday}]] に未完了タスクはありませんでした -->\n`;
    }
} else {
    tR += `<!-- 前日の日記: [[${yesterday}]] が見つかりませんでした -->\n`;
}
%>

## 今日の予定
- 

## タスク
- [ ] 

## メモ
- 

## 振り返り
- よかった点:
- 改善点:

