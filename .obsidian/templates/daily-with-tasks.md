# 📅 <% tp.date.now("YYYY-MM-DD") %> の振り返り

## 🔄 前日からの引き継ぎタスク
<%*
// 前日の日付を計算
const yesterday = moment(tp.file.title).subtract(1, 'days').format('YYYY-MM-DD');
const yesterdayFile = tp.file.find_tfile(yesterday);

if (yesterdayFile) {
    const content = await tp.file.include(yesterdayFile.path);
    // 未完了のタスク（- [ ] で始まる行）を抽出
    const lines = content.split('\n');
    const incompleteTasks = lines.filter(line => {
        const trimmed = line.trim();
        return trimmed.startsWith('- [ ]') || trimmed.startsWith('- [x]') === false;
    });
    
    if (incompleteTasks.length > 0) {
        tR += `<!-- 前日の日記: [[${yesterday}]] から引き継ぎ -->\n`;
        incompleteTasks.forEach(task => {
            // 完了済みタスクは未完了に戻す
            const taskText = task.replace(/^- \[x\]/, '- [ ]');
            tR += taskText + '\n';
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



