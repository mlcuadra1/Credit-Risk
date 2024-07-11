import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def draw_mean_median(df, col, axes, i):
    """
    Function for drawing a mean and median line.
    Arg: df['column']
    """
    print(str(i), '| mean: ', df[col].mean(), ' | median:', df[col].median())
    axes[i].axvline(x=df[col].mean(), color='red', label='mean')
    axes[i].axvline(x=df[col].median(), color='green', ls='--', label='median')

def trim_axs(axs, N):
    """
    Reduce *axs* to *N* Axes. All further Axes are removed from the figure.
    """
    axs = axs.flat
    for ax in axs[N:]:
        ax.remove()
    return axs[:N]

def multi_dtype_plot(df: pd.DataFrame, col_list: list, nrows: int, ncols: int, size='big', xtick_rotation=0, align='right', wspace=0.2, hspace=0.2):
    """
    Plots different types of columns in a grid of subplots.

    Parameters:
    df (pd.DataFrame): The dataframe containing the data.
    col_list (list): List of column names to plot.
    nrows (int): Number of rows in the subplot grid.
    ncols (int): Number of columns in the subplot grid.
    xtick_rotation (int, optional): Degrees to rotate the x-tick labels. Default is 0.
    """    
    if size == 'big':
        figsize=(14, 10)
    elif size == 'wide':
        figsize=(14, 4)

    fig, axes = plt.subplots(nrows, ncols, figsize=figsize)
    axes = trim_axs(axes, len(col_list))  # Trim axes to the number of columns

    for i, col in enumerate(col_list):
        if df[col].dtypes == 'object':
            sns.countplot(x=df[col], data=df, ax=axes[i])
            axes[i].set_ylabel('')
            axes[i].set_xticklabels(axes[i].get_xticklabels(), rotation=xtick_rotation, horizontalalignment=align)
        elif df[col].dtypes == 'int64' or df[col].dtypes == 'float64':
            sns.histplot(x=df[col], ax=axes[i], bins=20)
            draw_mean_median(df, col, axes, i)  # Fixed call to draw_mean_median
            axes[i].set_ylabel('')

    fig.subplots_adjust(wspace=wspace, hspace=hspace)
    return fig, axes
