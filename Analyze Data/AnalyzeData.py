import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

def analyze_data(input_file, output_dir="analysis_results"):
    """
    Perform comprehensive analysis of the crop recommendation dataset.
    
    Args:
        input_file (str): Path to the cleaned CSV file
        output_dir (str): Directory to save analysis plots
    """
    try:
        # Create output directory
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Read the cleaned dataset
        df = pd.read_csv(input_file)
        print("Dataset Shape:", df.shape)
        print("\nDataset Info:")
        print(df.info())
        
        # 1. Class Distribution Analysis
        plt.figure(figsize=(12, 6))
        class_counts = df['label'].value_counts()
        sns.barplot(x=class_counts.index, y=class_counts.values)
        plt.title('Distribution of Crop Types')
        plt.xticks(rotation=45, ha='right')
        plt.xlabel('Crop Type')
        plt.ylabel('Count')
        plt.tight_layout()
        plt.savefig(output_path / 'class_distribution.png')
        plt.close()
        
        print("\nClass Distribution:")
        print(class_counts)
        print("\nClass Balance Metrics:")
        print(f"Number of unique classes: {len(class_counts)}")
        print(f"Most common class: {class_counts.index[0]} ({class_counts.iloc[0]} samples)")
        print(f"Least common class: {class_counts.index[-1]} ({class_counts.iloc[-1]} samples)")
        
        # 2. Numerical Features Analysis
        numerical_cols = df.select_dtypes(include=[np.number]).columns
        numerical_cols = [col for col in numerical_cols if col != 'label']
        
        # Create histograms for numerical features
        n_cols = 3
        n_rows = (len(numerical_cols) + n_cols - 1) // n_cols
        fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 4*n_rows))
        axes = axes.flatten()
        
        for idx, col in enumerate(numerical_cols):
            sns.histplot(data=df, x=col, hue='label', multiple="stack", ax=axes[idx])
            axes[idx].set_title(f'Distribution of {col}')
            axes[idx].tick_params(axis='x', rotation=45)
        
        # Hide empty subplots
        for idx in range(len(numerical_cols), len(axes)):
            axes[idx].set_visible(False)
            
        plt.tight_layout()
        plt.savefig(output_path / 'numerical_distributions.png')
        plt.close()
        
        # 3. Correlation Analysis
        plt.figure(figsize=(12, 10))
        correlation_matrix = df[numerical_cols].corr()
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, fmt='.2f')
        plt.title('Correlation Matrix of Numerical Features')
        plt.tight_layout()
        plt.savefig(output_path / 'correlation_heatmap.png')
        plt.close()
        
        # 4. Box Plots for each numerical feature by crop type
        plt.figure(figsize=(15, 10))
        df_melted = pd.melt(df, id_vars=['label'], value_vars=numerical_cols)
        sns.boxplot(x='label', y='value', hue='variable', data=df_melted)
        plt.title('Distribution of Features by Crop Type')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig(output_path / 'feature_boxplots.png')
        plt.close()
        
        # 5. Statistical Summary
        print("\nStatistical Summary of Numerical Features:")
        print(df[numerical_cols].describe())
        
        # 6. Pairplot for top correlated features
        # Get top 5 most correlated feature pairs
        corr_pairs = correlation_matrix.unstack().sort_values(ascending=False)
        top_corr_pairs = corr_pairs[corr_pairs < 1.0].head(5)
        top_features = list(set([pair[0] for pair in top_corr_pairs.index] + 
                              [pair[1] for pair in top_corr_pairs.index]))
        
        plt.figure(figsize=(12, 10))
        sns.pairplot(df[top_features + ['label']], hue='label', diag_kind='kde')
        plt.savefig(output_path / 'feature_pairplot.png')
        plt.close()
        
        print("\nTop 5 Most Correlated Feature Pairs:")
        print(top_corr_pairs)
        
        # 7. Save summary statistics to CSV
        summary_stats = df.groupby('label')[numerical_cols].agg(['mean', 'std', 'min', 'max'])
        summary_stats.to_csv(output_path / 'crop_statistics.csv')
        
        print(f"\nAnalysis complete! Results saved to {output_dir}/")
        
    except Exception as e:
        print(f"An error occurred during analysis: {str(e)}")

if __name__ == "__main__":
    input_file = "data/cleanCrop_rec_DataSet.csv"
    analyze_data(input_file)
