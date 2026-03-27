import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os

# Criar a pasta 'figures' se não existir
os.makedirs('figures', exist_ok=True)

# Configuração global de estilo académico
sns.set_theme(style="whitegrid", context="paper", font_scale=1.2)
# Usando o nome MARTA como exemplo, podes alterar para PyMAGE ou outro
TOOL_NAME = "MARTA (Gen 3)" 
BASELINE_NAME = "Monolithic Baseline"

# ==========================================
# FIGURA 1: Robustness & Executability
# ==========================================
def plot_robustness():
    # Dados globais (Somas)
    data = {
        'Metric': ['Executable Tests\n(Passing)', 'Executable Tests\n(Passing)', 'Hallucinated/Broken\nAssertions', 'Hallucinated/Broken\nAssertions'],
        'Approach': [BASELINE_NAME, TOOL_NAME, BASELINE_NAME, TOOL_NAME],
        'Count': [220, 2020, 5932, 4355]
    }
    df = pd.DataFrame(data)

    fig, ax = plt.subplots(figsize=(8, 5))
    
    # Cores contrastantes (Azul para Baseline, Laranja para a tua ferramenta)
    palette = {BASELINE_NAME: "#4C72B0", TOOL_NAME: "#DD8452"}
    
    sns.barplot(x='Metric', y='Count', hue='Approach', data=df, ax=ax, palette=palette)
    
    # Adicionar os números em cima das barras para impacto
    for p in ax.patches:
        ax.annotate(format(p.get_height(), '.0f'), 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha = 'center', va = 'center', 
                    xytext = (0, 9), 
                    textcoords = 'offset points',
                    fontweight='bold')

    ax.set_ylabel('Total Count (10 Projects)')
    ax.set_xlabel('')
    ax.set_title('Assertion Robustness: Valid vs Hallucinated Tests', pad=15, fontweight='bold')
    
    # Ajustar a legenda para o canto superior esquerdo (upper left)
    plt.legend(title='Generation Approach', loc='upper left')
    plt.tight_layout()
    plt.savefig('figures/robustness.pdf', format='pdf', bbox_inches='tight')
    plt.close()
    print("✅ Figure 1 generated: robustness.pdf")

# ==========================================
# FIGURA 2: Project-by-Project Effectiveness
# ==========================================
def plot_project_effectiveness():
    # Dados projeto a projeto (Temp 0.2)
    projects = ['python-string-utils', 'pytutils', 'superstring.py', 'codetiming', 
                'isort', 'sty', 'pyMonet', 'flutes', 'dataclasses-json', 'docstring_parser']
    
    stmt_base = [80.10, 33.14, 41.76, 85.00, 41.49, 87.63, 68.46, 51.21, 46.82, 46.42]
    stmt_react = [85.74, 42.67, 62.35, 73.33, 54.95, 91.75, 91.28, 58.34, 44.50, 45.30]
    
    mut_base = [55.28, 16.80, 6.25, 40.91, 11.33, 28.26, 41.71, 27.57, 20.22, 23.12]
    mut_react = [59.63, 28.57, 23.96, 19.70, 16.52, 50.00, 59.30, 67.29, 15.03, 18.24]
    
    # Preparar DataFrame
    df_plot = pd.DataFrame({
        'Project': projects * 2,
        'Approach': [BASELINE_NAME]*10 + [TOOL_NAME]*10,
        'Statement Coverage (%)': stmt_base + stmt_react,
        'Mutation Score (%)': mut_base + mut_react
    })

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    palette = {BASELINE_NAME: "#4C72B0", TOOL_NAME: "#55A868"} # Azul e Verde
    
    # Plot 1: Statement Coverage
    sns.barplot(x='Statement Coverage (%)', y='Project', hue='Approach', data=df_plot, ax=axes[0], palette=palette)
    axes[0].set_title('(a) Statement Coverage by Project', fontweight='bold')
    axes[0].set_xlabel('Statement Coverage (%)')
    axes[0].set_ylabel('')
    axes[0].legend_.remove() # Remover legenda para não duplicar

    # Plot 2: Mutation Score
    sns.barplot(x='Mutation Score (%)', y='Project', hue='Approach', data=df_plot, ax=axes[1], palette=palette)
    axes[1].set_title('(b) Mutation Score by Project', fontweight='bold')
    axes[1].set_xlabel('Mutation Score (%)')
    axes[1].set_ylabel('')
    axes[1].legend(title='Approach', bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.tight_layout()
    plt.savefig('figures/project_effectiveness.pdf', format='pdf', bbox_inches='tight')
    plt.close()
    print("✅ Figure 2 generated: project_effectiveness.pdf")

# ==========================================
# FIGURA 3: Ablation Effect
# ==========================================
def plot_ablation():
    # Médias globais Temp 0.2
    data = {
        'Metric': ['Statement Cov (%)', 'Statement Cov (%)', 'Statement Cov (%)',
                   'Branch Cov (%)', 'Branch Cov (%)', 'Branch Cov (%)',
                   'Mutation Score (%)', 'Mutation Score (%)', 'Mutation Score (%)'],
        'Configuration': ['Baseline', 'Gen 1 (Inner Loop)', 'Gen 3 (Outer Loop)',
                          'Baseline', 'Gen 1 (Inner Loop)', 'Gen 3 (Outer Loop)',
                          'Baseline', 'Gen 1 (Inner Loop)', 'Gen 3 (Outer Loop)'],
        'Score': [58.20, 55.30, 65.02, 
                  46.54, 39.95, 52.68, 
                  27.14, 28.02, 35.82]
    }
    df = pd.DataFrame(data)

    fig, ax = plt.subplots(figsize=(9, 5))
    
    # Paleta progressiva (Azul para baseline, Laranja claro para Gen 1, Laranja forte para Gen 3)
    palette = {'Baseline': "#4C72B0", 'Gen 1 (Inner Loop)': "#F5B882", 'Gen 3 (Outer Loop)': "#C44E52"}
    
    sns.barplot(x='Metric', y='Score', hue='Configuration', data=df, ax=ax, palette=palette)
    
    # Anotações
    for p in ax.patches:
        ax.annotate(format(p.get_height(), '.1f'), 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha = 'center', va = 'center', 
                    xytext = (0, 7), 
                    textcoords = 'offset points',
                    fontsize=10)

    ax.set_ylim(0, 80) # Dá espaço para as labels
    ax.set_ylabel('Percentage Score (%)')
    ax.set_xlabel('')
    ax.set_title('Ablation Study: Performance Gains Across Configurations', pad=15, fontweight='bold')
    
    # Ajustar a legenda para o canto superior direito (upper right)
    plt.legend(title='System Configuration', loc='upper right')
    plt.tight_layout()
    plt.savefig('figures/ablation_effect.pdf', format='pdf', bbox_inches='tight')
    plt.close()
    print("✅ Figure 3 generated: ablation_effect.pdf")

# Correr as funções
if __name__ == "__main__":
    print("Generating academic figures...")
    plot_robustness()
    plot_project_effectiveness()
    plot_ablation()
    print("All figures successfully saved in the 'figures/' directory.")