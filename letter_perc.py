# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 15:32:01 2022

@author: Hakan
"""

def letter_perc(df1, df2, columns_list=["mean_letter_df1","mean_letter_df2","df1_percentage","df2_percentage"], bar_plot=False, pie_chart=False):
    """
    letter_of_songs_v1.1
    calculation of percentage of the letters and grpahs.

    Args:
        df1 : first dataframe
        df2: second dataframe 
        columns_list = name of the columns. first two variable names show mean of
                      dataframes, last two variable names show percentage
        bar_plot: if True, it creates bar plot graphs of two dataframes, side by side
        pie_chart: if True, it creates pie charts of two dataframes, side by side
    Returns:
        df_perc : dataframe include mean and percentages variables of dataframes
        
    Note:
        This function for create dataframe and make graphs
        example:
            df_perc = letter_perc(df_pop,df_rock, \
                      columns_list=["mean_pop_letter","mean_rock_letter",\
                     "pop_percentage","rock_percentage"],\
                      bar_plot=True, pie_chart=False)
        
    """
    import pandas as pd
    
    df_perc = pd.concat([pd.DataFrame(df1.loc[:,"A":"Z"].apply(lambda x: x.mean(),axis=0), columns=[columns_list[0]])\
                        ,pd.DataFrame(df2.loc[:,"A":"Z"].apply(lambda x: x.mean(),axis=0), columns=[columns_list[1]])]\
                        ,axis=1)
    
    df_perc[columns_list[2]]  = df_perc[columns_list[0]] / df_perc[columns_list[0]].sum() * 100
    df_perc[columns_list[3]]  = df_perc[columns_list[1]] / df_perc[columns_list[1]].sum() * 100
    
    
    

    if bar_plot:
        
        import matplotlib.pyplot as plt
        plt.style.use('seaborn')

        df1= df_perc.loc[:,columns_list[2]].sort_values()
        df2 = df_perc.loc[:,columns_list[3]].sort_values()


        fig, (ax, ax2)  = plt.subplots(nrows=1, ncols=2, figsize=(15,10))

        ax.invert_xaxis()
        ax.yaxis.tick_right()


        df1.plot(kind='barh', x='LABEL',  legend=False, ax=ax)
        df2.plot(kind='barh', x='LABEL', ax=ax2)


        ax.set_xlabel('percentage [%]')
        ax2.set_xlabel('percentage [%]')
        ax.set_ylabel("LETTERS", fontweight='bold')

        ax.set_title(columns_list[2]+ "of the Each Letter in lyrics ",fontweight='bold')
        ax2.set_title(columns_list[3]+ "of the Each Letter",fontweight='bold')
        
        plt.show()
        
    if pie_chart:
        
        fig = plt.figure(figsize=(15,10))


        ax1 = fig.add_subplot(121)
        ax1.pie(df_perc[columns_list[2]], labels = df_perc.index, startangle = 90, shadow = False)

        ax2 = fig.add_subplot(122)
        ax2.pie(df_perc[columns_list[3]], labels = df_perc.index, startangle = 90, shadow = False)

        ax1.set_title(columns_list[2]+ " of the Each Letter in lyrics\n ",fontweight='bold')
        ax2.set_title(columns_list[3]+ " of the Each Letter\n",fontweight='bold')

        plt.show()
        
    return df_perc