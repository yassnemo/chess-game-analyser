import matplotlib.pyplot as plt
import seaborn as sns

def plot_accuracy(analysis_df):
    """Plot centipawn loss over time"""
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='ply', y='cpl', hue='turn', data=analysis_df)
    plt.title('Move Accuracy (Centipawn Loss)')
    plt.xlabel('Move Number')
    plt.ylabel('Centipawn Loss')
    return plt.gcf()

def plot_heatmap(analysis_df):
    """Create move heatmap by piece type"""
    # Extract piece from FEN (second part of FEN string)
    analysis_df['piece'] = analysis_df['fen'].apply(lambda x: x.split(' ')[1])
    
    plt.figure(figsize=(10, 8))
    heatmap_data = analysis_df.groupby(['turn', 'piece']).size().unstack().fillna(0)
    sns.heatmap(heatmap_data, annot=True, fmt='g')
    plt.title('Piece Movement Heatmap')
    return plt.gcf()