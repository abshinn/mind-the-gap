
import pandas as pd
import numpy as np


columns = [u'essay_title', u'_projectid', u'date_completed', u'date_expired', u'funding_status', 
           u'grade_level', u'num_donors', u'date_posted', u'poverty_level', u'students_reached', 
           u'project_subject', u'subject_category', u'total_donations', u'tot_price_without_support', 
           u'total_price_with_support', u'_schoolid', u'city', u'state', u'district', u'latitude', 
           u'longitude', u'teach_for_america', u'_teacherid', u'zip', u'_NCESid', u'resource_type', u'county']

df = pd.read_csv("data/looker_completed_projects_7_14_14.csv", skiprows=1, names=columns,
                 parse_dates = ["date_posted", "date_completed", "date_expired"],
                 true_values="Yes", false_values="No")

# df["NCESid"] = df._NCESid.dropna().drop_duplicates().astype(np.int)


df.groupby("_schoolid").NCESid.head()


df.funding_status.value_counts()


# Out[4]:

#     completed      435665
#     expired        181882
#     reallocated      6043
#     dtype: int64

# In[5]:

for column in sorted(columns):
    print column


# Out[5]:

#     _NCESid
#     _projectid
#     _schoolid
#     _teacherid
#     city
#     county
#     date_completed
#     date_expired
#     date_posted
#     district
#     essay_title
#     funding_status
#     grade_level
#     latitude
#     longitude
#     num_donors
#     poverty_level
#     project_subject
#     resource_type
#     state
#     students_reached
#     subject_category
#     teach_for_america
#     tot_price_without_support
#     total_donations
#     total_price_with_support
#     zip
# 

# In[95]:

print "Date Posted Range:\n{} - {}\n".format(df.date_posted.min(), df.date_posted.max())


# Out[95]:
# ## Amount of projects per semester

# # State Finance

# In[127]:

# stdf = pd.read_csv("data/stats/stfis111a.txt", sep='\t')
# stdf.head()

# Be Careful When Aggregating!
# missing data are -1
# not applicable are -2
# suppressed are -9

# Out[127]:

#     columns.tsv       [31mstfis111a.txt[m[m     stfis111a_txt.zip stfis111alay.txt
# 

#         SURVYEAR  FIPS STABR                    STNAME          R1A         R1B  \
#     0       2011     1    AL                   Alabama           -2          -2   
#     1       2011     2    AK                    Alaska           -2          -2   
#     2       2011     4    AZ                   Arizona   3094295196          -2   
#     3       2011     5    AR                  Arkansas   1449957675     1515281   
#     4       2011     6    CA                California  16065608103   729009639   
#     5       2011     8    CO                  Colorado   3470847843    45894241   
#     6       2011     9    CT               Connecticut           -2          -2   
#     7       2011    10    DE                  Delaware    435580555          -2   
#     8       2011    11    DC      District of Columbia           -2          -2   
#     9       2011    12    FL                   Florida  10549647585   531731043   
#     10      2011    13    GA                   Georgia   5650262817  1637335449   
#     11      2011    15    HI                    Hawaii           -2          -2   
#     12      2011    16    ID                     Idaho    412701378     3521511   
#     13      2011    17    IL                  Illinois  14482299767   752096688   
#     14      2011    18    IN                   Indiana   2571966516     3849780   
#     15      2011    19    IA                      Iowa   1913657176   543778795   
#     16      2011    20    KS                    Kansas   1537067871          -2   
#     17      2011    21    KY                  Kentucky   1584905135   407105962   
#     18      2011    22    LA                 Louisiana   1339367237  1643520272   
#     19      2011    23    ME                     Maine    697940550          -2   
#     20      2011    24    MD                  Maryland           -2          -2   
#     21      2011    25    MA             Massachusetts           -2          -2   
#     22      2011    26    MI                  Michigan   5182018166    10144874   
#     23      2011    27    MN                 Minnesota   2498019143          -2   
#     24      2011    28    MS               Mississippi   1132741956     2943977   
#     25      2011    29    MO                  Missouri   4563463391   553992911   
#     26      2011    30    MT                   Montana    402719588     4168595   
#     27      2011    31    NE                  Nebraska   1844669246    26775582   
#     28      2011    32    NV                    Nevada   1209582956  1024728935   
#     29      2011    33    NH             New Hampshire   1293060387          -2   
#     30      2011    34    NJ                New Jersey  13665699940        5391   
#     31      2011    35    NM                New Mexico    480052957          -2   
#     32      2011    36    NY                  New York  16256074176   295763701   
#     33      2011    37    NC            North Carolina           -2          -2   
#     34      2011    38    ND              North Dakota    331542458     6998464   
#     35      2011    39    OH                      Ohio   8514889120   351472632   
#     36      2011    40    OK                  Oklahoma   1529147806          -2   
#     37      2011    41    OR                    Oregon   1983254738     1589238   
#     38      2011    42    PA              Pennsylvania  11633093396  1810806318   
#     39      2011    44    RI              Rhode Island           -2          -2   
#     40      2011    45    SC            South Carolina   1693515194   128678129   
#     41      2011    46    SD              South Dakota    552135651          -2   
#     42      2011    47    TN                 Tennessee           -2          -2   
#     43      2011    48    TX                     Texas  20382781762   260843147   
#     44      2011    49    UT                      Utah   1263423289   110400896   
#     45      2011    50    VT                   Vermont      1276311     2361644   
#     46      2011    51    VA                  Virginia           -2          -2   
#     47      2011    53    WA                Washington   3049440102      609970   
#     48      2011    54    WV             West Virginia    922414570    15357476   
#     49      2011    55    WI                 Wisconsin   4691950365          -2   
#     50      2011    56    WY                   Wyoming    417124141     4715116   
#     51      2011    60    AS            American Samoa           -2          -2   
#     52      2011    66    GU                      Guam           -2   189039116   
#     53      2011    69    MP  Northern Mariana Islands           -2          -2   
#     54      2011    72    PR               Puerto Rico           -2          -2   
#     55      2011    78    VI            Virgin Islands           -2          -2   
#     
#                 R1C         R1D        R1E         R1F       R1G        R1H  \
#     0    1070276399   542310716    4198317      701516         0       2504   
#     1     297717875   160752197     131258       88690         0          0   
#     2            -2    48737042    3951044    22923249    145062    7321458   
#     3            -2     3833118    8629306     3575452     91384     155355   
#     4        168400          -2     431760   261358537  18216201   38379342   
#     5            -2          -2   66470976     5926171   6371156     104609   
#     6    5568316704          -2    3288337   208902080         0   11149366   
#     7            -2          -2          0    59404585         0          0   
#     8     553482069  1074406370     797904           0    119582          0   
#     9            -2          -2     580847           0  11678234    7219905   
#     10    156181199          -2   22400657     2134897   3412097          0   
#     11           -2          -2          0           0   2724418          0   
#     12           -2          -2    2604283      274260   1535730          0   
#     13           -2          -2   20138742   467317608  11693346   18001008   
#     14    238043561    59555455    8665463    15289766    155854    4268444   
#     15           -2          -2    7757257   218099028   2131320    1663729   
#     16           -2          -2    4521855   269630386    449080          0   
#     17           -2    35822440    4473678       10611       100          0   
#     18           -2          -2   12742679     1647743     16486     706052   
#     19    493127060      470068    4417214    42676937     50527    1152245   
#     20   3173859462  3114621967    9623404     4863085   2089375          0   
#     21   7801657290          -2    3324046   137324402    679137          0   
#     22       624478    12406267   20732616    56574640  10711349   46033904   
#     23           -2          -2   98614958   155915535   2153272          0   
#     24           -2    19921046    4166209     3795361    825684     554721   
#     25           -2          -2   25856287    67129463    700214    5288117   
#     26           -2          -2    1863270     1585256    104238     616303   
#     27           -2          -2    1453860     3981875     69308      27197   
#     28           -2     1387463    8181475      110577    988965      12263   
#     29    228210587          -2    5557751   103344098    260041     329839   
#     30           -2          -2   11723823   809453967   3969196  186544220   
#     31           -2     1020925    2774649           0         0          0   
#     32  10086390209          -2   35208492   313986402         0    3818720   
#     33   2737195244   183705162    5205591           0         0          0   
#     34           -2     1309490     804359    41833794    171538      38363   
#     35           -2          -2  113079906   700215119   7395832    1181059   
#     36           -2   104677386   17630333     1988793   2089662          0   
#     37      3577324          -2   11746993     7273104   1665815      88908   
#     38           -2          -2   52179992  2081187421         0    2680771   
#     39   1166220484      817675    1184735    24313822     30461      63045   
#     40    883837441   168005440    7429878    12014029    511573      36562   
#     41           -2    21971113     867119     1064057    120720          0   
#     42   1754305830  1113904613    5243160      595435    132731     441319   
#     43           -2          -2   77255037    12554019         0          0   
#     44           -2          -2  121234526      645733   1706667    1506360   
#     45           -2      648623    2352907   126769947      4145    3849428   
#     46   4655901744  2513945231   24595600   302140240   3235521          0   
#     47      9351043      785944   80390357    85747607         0    3868684   
#     48       474904      876399    2557701      482914         0     619707   
#     49     22275346          -2    2891242   249704014    652321    2823575   
#     50           -2          -2      99689     3061391     15569        360   
#     51           -2          -2          0           0         0          0   
#     52           -2          -2          0           0         0          0   
#     53           -2          -2          0           0         0          0   
#     54           -2          -2          0           0         0          0   
#     55           -2          -2      47911           0         0          0   
#     
#               R1I        R1J        R1K         R1L       R1M       R1N  \
#     0    19998054  118329978  182375416   332034882   1072250         0   
#     1     4151981   11378331    9998478    37637881         0         0   
#     2    24330805  109872955  111557843   540528325    638298   7774353   
#     3    20648007   55712979   79415073    88181206     33078    231354   
#     4   347874973  427143116          0  2615474811         0         0   
#     5    22317597   92698201  156308274   402422964   4214924   2834127   
#     6      135386  108369711          0    59023710         0    592417   
#     7     2683990   15758661     896050    61359467         0         0   
#     8      676626    1290439    6915483    59409656      5535   1522125   
#     9    91963384  304353457  626838780   374144624   1975272         0   
#     10   24886755  195510380  253582926   261771907     26089   3380618   
#     11          0   27470945    1112698    30159880         0   1811803   
#     12    3282355   26373559    3083126    42512123         0         0   
#     13   97770245  251985421   90800453   864694953  98522952  21048512   
#     14   16997448  199874632   68818887   942403898  55303677         0   
#     15   11783120  108814261    8152878   130999400  11455303   1276236   
#     16   10659493   85408157   33689038   235230449  13420902   1669498   
#     17   16933031  104890332     955900    65120526    986050     36595   
#     18   35550856   51009487          0   148508510    590207   2507143   
#     19    1189022   32876906    2006669    23445894     80182    152094   
#     20    1869326  114921289  150385784   101968649         0   3428682   
#     21    1723790  141785948   36141634   280173188         0  21687769   
#     22   35960887  189700438   66951173   499716281         0   2193997   
#     23   94423444  189344153   31649572   523519727         0         0   
#     24   22087837   54262632   53317062   113398268         0    437215   
#     25   80536794  146700877  174403333   193790341         0         0   
#     26    5168942   19287942   36763848    26517392    188132    444158   
#     27    5914143   70048233   84243645    37857621         0    378342   
#     28   20428055   29155516    1660011    62480400       447   2186271   
#     29    2119685   39887121    1765436    26004133    307622    462810   
#     30    3675489  257464720  284879965   248618138         0   1125445   
#     31   13511583   24272062   21695459    51707428      5217    554104   
#     32   73679012  295142076   15248644  1721650670    175694   3129660   
#     33   10028247  240145189          0   225145447         0         0   
#     34    3679728   25006560   24656771    28796233         0    174314   
#     35   50600954  281325899  262512392   603916817  10907136   6035409   
#     36   16824064   75448160  151144781   101324672    369235   1185694   
#     37   16806328   47362641   88960859   230676265    185091    658791   
#     38   40050383  342031894   29276981   561252708         0   4257172   
#     39     437551   15920659    2132464    10787629     66818    555067   
#     40   42480993   86160755  144479335   214356934         0   2175124   
#     41    4902419   27959911    5727966    32204902         0   2445564   
#     42    4322097  150474479  280080547   298109550         0   1545987   
#     43  105419002  642806284  247131413   639991746         0         0   
#     44   13766053   65237758    3606672    98330345   1523149         0   
#     45    5734648   18464517    1031899    93542153      1159     73381   
#     46    4528044  236376531          0   221956285    278534   7206099   
#     47   26461792  112010786  122521302   273787688         0   2125387   
#     48    5775286   23607536    1903239    60120094    145641    317375   
#     49   10152775  163779132   52984397   187552609   3086749   1864288   
#     50    3012563   16851830    1317966    13456880         0     90465   
#     51          0          0      36964      187572         0         0   
#     52          0     793281          0      636287         0         0   
#     53          0          0          0           0         0         0   
#     54          0      42438          0         403         0         0   
#     55          0          0          0   198343971         0         0   
#     
#                STR1         R2      
#     0    2270596012   37386814 ...  
#     1     521768001          0 ...  
#     2    3941830923  258379586 ...  
#     3    1708248461    3137888 ...  
#     4   20203927003          0 ...  
#     5    4270380303   17914122 ...  
#     6    5739726265          0 ...  
#     7     516278723          0 ...  
#     8    1698625789          0 ...  
#     9   12492913226          0 ...  
#     10   8208750894          0 ...  
#     11     63279744          0 ...  
#     12    495614065          0 ...  
#     13  16691051079          0 ...  
#     14   4165635171   15472734 ...  
#     15   2739805746    2290964 ...  
#     16   1922116343  106229058 ...  
#     17   2221229749          0 ...  
#     18   3233812877          0 ...  
#     19   1255756186     863851 ...  
#     20   6672767938          0 ...  
#     21   8287172802          0 ...  
#     22   6031160526   11634673 ...  
#     23   3437724269  197923615 ...  
#     24   1404101886    1164769 ...  
#     25   5739444148   39752117 ...  
#     26    497226105  135414971 ...  
#     27   2071409980   19330603 ...  
#     28   2360780494          0 ...  
#     29   1597635573          0 ...  
#     30  14477162107      29070 ...  
#     31    595594384    2946189 ...  
#     32  28782462334  289716374 ...  
#     33   3401424880          0 ...  
#     34    423139915   19211010 ...  
#     35  10202136097  146370951 ...  
#     36   1999841793  125718385 ...  
#     37   2386484083   76747113 ...  
#     38  14472948844    4014992 ...  
#     39   1198153543          0 ...  
#     40   3371630796    1471502 ...  
#     41    648335365   12852307 ...  
#     42   3608118994          0 ...  
#     43  22356228391  120184333 ...  
#     44   1679229355          0 ...  
#     45    125491387          0 ...  
#     46   7668023589          0 ...  
#     47   3677484371          0 ...  
#     48   1033550221     149998 ...  
#     49   5137189224          0 ...  
#     50    456684219  156939141 ...  
#     51       224536          0 ...  
#     52    190468684          0 ...  
#     53            0          0 ...  
#     54        42841          0 ...  
#     55    198391882          0 ...  
#     
#     [56 rows x 314 columns]

# In[128]:

col_description = pd.read_csv("data/stats/columns.tsv", sep='\t\t', index_col=0)
col_description


# Out[128]:

#              type order                                        Description
#     name                                                                  
#     SURVYEAR    N     1                       FISCAL YEAR OF SURVEY (2011)
#     FIPS       AN     2  AMERICAN NATIONAL STANDARDS INSTITUTE (ANSI) S...
#     STABR      AN     3                    POSTAL STATE ABBREVIATION CODES
#     STNAME     AN     4                     NAME OF THE STATE OR TERRITORY
#     R1A         N     5                        LOCAL REVENUES PROPERTY TAX
#     R1B         N     6                     LOCAL REVENUES NONPROPERTY TAX
#     R1C         N     7       LOCAL REVENUES LOCAL GOVERNMENT PROPERTY TAX
#     R1D         N     8    LOCAL REVENUES LOCAL GOVERNMENT NONPROPERTY TAX
#     R1E         N     9                  LOCAL REVENUES INDIVIDUAL TUITION
#     R1F         N    10                   LOCAL REVENUES TUITION FROM LEAS
#     R1G         N    11  LOCAL REVENUES TRANSPORTATION FEES FROM INDIVI...
#     R1H         N    12       LOCAL REVENUES TRANSPORTATION FEES FROM LEAS
#     R1I         N    13             LOCAL REVENUES EARNINGS ON INVESTMENTS
#     R1J         N    14                        LOCAL REVENUES FOOD SERVICE
#     R1K         N    15                  LOCAL REVENUES STUDENT ACTIVITIES
#     R1L         N    16                      LOCAL REVENUES OTHER REVENUES
#     R1M         N    17                   LOCAL REVENUES TEXTBOOK REVENUES
#     R1N         N    18                       LOCAL REVENUES SUMMER SCHOOL
#     STR1        N    19  LOCAL REVENUES SUBTOTAL  (equals R1A + R1B + R...
#     R2          N    20                              INTERMEDIATE REVENUES
#     R3          N    21                                     STATE REVENUES
#     R4A         N    22                     FEDERAL REVENUES DIRECT GRANTS
#     R4B         N    23                        FEDERAL REVENUES THRU STATE
#     R4C         N    24        FEDERAL REVENUES THRU INTERMEDIATE AGENCIES
#     R4D         N    25                     FEDERAL REVENUES OTHER SOURCES
#     STR4        N    26  FEDERAL REVENUES SUBTOTAL (equals R4A + R4B + ...
#     R5          N    27                        REVENUES FROM OTHER SOURCES
#     TR          N    28  TOTAL REVENUES FROM ALL SOURCES (equals STR1 +...
#     E11         N    29                INSTRUCTIONAL EXPENDITURES SALARIES
#     E12         N    30       INSTRUCTIONAL EXPENDITURES EMPLOYEE BENEFITS
#     E13         N    31      INSTRUCTIONAL EXPENDITURES PURCHASED SERVICES
#     E14         N    32  INSTRUCTIONAL EXPENDITURES TUITION TO PRIVATE ...
#     E15         N    33  INSTRUCTIONAL EXPENDITURES TUITION TO OTHER LE...
#     E16         N    34                INSTRUCTIONAL EXPENDITURES SUPPLIES
#     E17         N    35                INSTRUCTIONAL EXPENDITURES PROPERTY
#     E18         N    36                   INSTRUCTIONAL EXPENDITURES OTHER
#     STE1        N    37  INSTRUCTIONAL EXPENDITURES SUBTOTAL (equals E1...
#     E11A        N    38                  TEACHER SALARIES REGULAR PROGRAMS
#     E11B        N    39        TEACHER SALARIES SPECIAL EDUCATION PROGRAMS
#     E11C        N    40     TEACHER SALARIES VOCATIONAL EDUCATION PROGRAMS
#     E11D        N    41          TEACHER SALARIES OTHER EDUCATION PROGRAMS
#     E2          N    42               INSTRUCTIONAL EXPENDITURES TEXTBOOKS
#     E212        N    43  SUPPORT EXPENDITURES SALARIES STUDENT SUPPORT ...
#     E213        N    44  SUPPORT EXPENDITURES SALARIES INSTRUCTIONAL ST...
#     E214        N    45  SUPPORT EXPENDITURES SALARIES GENERAL ADMINIST...
#     E215        N    46  SUPPORT EXPENDITURES SALARIES SCHOOL ADMINISTR...
#     E216        N    47  SUPPORT EXPENDITURES SALARIES OPERATION & MAIN...
#     E217        N    48  SUPPORT EXPENDITURES SALARIES PUPIL TRANSPORTA...
#     E218        N    49       SUPPORT EXPENDITURES SALARIES OTHER SERVICES
#     TE21        N    50  SUPPORT EXPENDITURES SALARIES SUBTOTAL (equals...
#     E222        N    51  SUPPORT EXPENDITURES EMPLOYEE BENEFITS STUDENT...
#     E223        N    52  SUPPORT EXPENDITURES EMPLOYEE BENEFITS INSTRUC...
#     E224        N    53  SUPPORT EXPENDITURES EMPLOYEE BENEFITS GENERAL...
#     E225        N    54  SUPPORT EXPENDITURES EMPLOYEE BENEFITS SCHOOL ...
#     E226        N    55  SUPPORT EXPENDITURES EMPLOYEE BENEFITS OPERATI...
#     E227        N    56  SUPPORT EXPENDITURES EMPLOYEE BENEFITS PUPIL T...
#     E228        N    57  SUPPORT EXPENDITURES EMPLOYEE BENEFITS OTHER S...
#     TE22        N    58  SUPPORT EXPENDITURES EMPLOYEE BENEFITS SUBTOTA...
#     E232        N    59  SUPPORT EXPENDITURES PURCHASED SERVICES STUDEN...
#     E233        N    60  SUPPORT EXPENDITURES PURCHASED SERVICES INSTRU...
#               ...   ...                                                ...
#     
#     [314 rows x 3 columns]

schooldf = pd.read_csv("data/school/sc111a_supp.txt", sep='\t')
schooldf


#         SURVYEAR      NCESSCH  FIPST   LEAID  SCHNO STID SEASCH  \
#     0       2011  10000200277      1  100002    277  210     20   
#     1       2011  10000201402      1  100002   1402  210     25   
#     2       2011  10000201667      1  100002   1667  210     50   
#     3       2011  10000201670      1  100002   1670  210     60   
#     4       2011  10000201705      1  100002   1705  210     30   
#     5       2011  10000201706      1  100002   1706  210     40   
#     6       2011  10000201876      1  100002   1876  210      1   
#     7       2011  10000500870      1  100005    870  101     10   
#     8       2011  10000500871      1  100005    871  101     20   
#     9       2011  10000500879      1  100005    879  101    110   
#     10      2011  10000500889      1  100005    889  101    200   
#     11      2011  10000501616      1  100005   1616  101     35   
#     12      2011  10000502150      1  100005   2150  101      5   
#     13      2011  10000600193      1  100006    193   48    143   
#     14      2011  10000600872      1  100006    872   48     30   
#     15      2011  10000600876      1  100006    876   48     70   
#     16      2011  10000600877      1  100006    877   48     90   
#     17      2011  10000600878      1  100006    878   48    100   
#     18      2011  10000600880      1  100006    880   48    120   
#     19      2011  10000600883      1  100006    883   48    140   
#     20      2011  10000600887      1  100006    887   48    180   
#     21      2011  10000600986      1  100006    986   48    150   
#     22      2011  10000600987      1  100006    987   48    160   
#     23      2011  10000601413      1  100006   1413   48     95   
#     24      2011  10000601434      1  100006   1434   48     40   
#     25      2011  10000601585      1  100006   1585   48     42   
#     26      2011  10000601685      1  100006   1685   48    145   
#     27      2011  10000601812      1  100006   1812   48    105   
#     28      2011  10000700091      1  100007     91  158    820   
#     29      2011  10000700248      1  100007    248  158    360   
#     30      2011  10000700251      1  100007    251  158    400   
#     31      2011  10000700337      1  100007    337  158     70   
#     32      2011  10000700342      1  100007    342  158    815   
#     33      2011  10000701422      1  100007   1422  158    415   
#     34      2011  10000701456      1  100007   1456  158     10   
#     35      2011  10000701483      1  100007   1483  158    380   
#     36      2011  10000701738      1  100007   1738  158     80   
#     37      2011  10000701739      1  100007   1739  158    350   
#     38      2011  10000701740      1  100007   1740  158    365   
#     39      2011  10000701741      1  100007   1741  158    425   
#     40      2011  10000701742      1  100007   1742  158    760   
#     41      2011  10000701743      1  100007   1743  158    810   
#     42      2011  10000701825      1  100007   1825  158    821   
#     43      2011  10000702091      1  100007   2091  158    410   
#     44      2011  10000702186      1  100007   2186  158    420   
#     45      2011  10000800303      1  100008    303  169     75   
#     46      2011  10000800495      1  100008    495  169     82   
#     47      2011  10000800831      1  100008    831  169     80   
#     48      2011  10000800839      1  100008    839  169     85   
#     49      2011  10000800851      1  100008    851  169    220   
#     50      2011  10000801423      1  100008   1423  169     10   
#     51      2011  10000801485      1  100008   1485  169     20   
#     52      2011  10000801798      1  100008   1798  169     83   
#     53      2011  10000802097      1  100008   2097  169     30   
#     54      2011  10000802133      1  100008   2133  169     90   
#     55      2011  10000901403      1  100009   1403  600   9000   
#     56      2011  10000901404      1  100009   1404  600   9010   
#     57      2011  10000901405      1  100009   1405  600   9020   
#     58      2011  10000901406      1  100009   1406  600   9040   
#     59      2011  10001102094      1  100011   2094  167     10   
#              ...          ...    ...     ...    ...  ...    ...   
#     
#                          LEANM                            SCHNAM       PHONE  \
#     0   ALABAMA YOUTH SERVICES  SEQUOYAH SCH - CHALKVILLE CAMPUS  2056808574   
#     1   ALABAMA YOUTH SERVICES      EUFAULA SCH - EUFAULA CAMPUS  3346874441   
#     2   ALABAMA YOUTH SERVICES                             CAMPS  3342153850   
#     3   ALABAMA YOUTH SERVICES                           DET CTR  3342153850   
#     4   ALABAMA YOUTH SERVICES     WALLACE SCH - MT MEIGS CAMPUS  3342156039   
#     5   ALABAMA YOUTH SERVICES         MCNEEL SCH - VACCA CAMPUS  2058384981   
#     6   ALABAMA YOUTH SERVICES            ALABAMA YOUTH SERVICES  2056825300   
#     7         ALBERTVILLE CITY             ALA AVENUE MIDDLE SCH  2568782341   
#     8         ALBERTVILLE CITY              ALBERTVILLE HIGH SCH  2568786580   
#     9         ALBERTVILLE CITY                    EVANS ELEM SCH  2568787698   
#     10        ALBERTVILLE CITY              ALBERTVILLE ELEM SCH  2568786611   
#     11        ALBERTVILLE CITY       BIG SPRING LAKE KINDERG SCH  2568787922   
#     12        ALBERTVILLE CITY           ALBERTVILLE PRIMARY SCH  2568786611   
#     13         MARSHALL COUNTY      KATE DUNCAN SMITH DAR MIDDLE  2567285950   
#     14         MARSHALL COUNTY                        ASBURY SCH  2568784068   
#     15         MARSHALL COUNTY            CLAYSVILLE JR HIGH SCH  2565824444   
#     16         MARSHALL COUNTY                  DOUGLAS ELEM SCH  2565934420   
#     17         MARSHALL COUNTY                  DOUGLAS HIGH SCH  2565932810   
#     18         MARSHALL COUNTY                   GRASSY ELEM SCH  2567532246   
#     19         MARSHALL COUNTY         KATE D SMITH DAR HIGH SCH  2567284238   
#     20         MARSHALL COUNTY              UNION GROVE ELEM SCH  2567532532   
#     21         MARSHALL COUNTY                  MARSHALL ALT SCH  2565827554   
#     22         MARSHALL COUNTY                 MARSHALL TECH SCH  2565825629   
#     23         MARSHALL COUNTY           ROBERT D SLOMAN PRIMARY  2565934912   
#     24         MARSHALL COUNTY            BRINDLEE MT MIDDLE SCH  2567532820   
#     25         MARSHALL COUNTY              BRINDLEE MT HIGH SCH  2567532800   
#     26         MARSHALL COUNTY         KATE D SMITH DAR ELEM SCH  2567282226   
#     27         MARSHALL COUNTY                DOUGLAS MIDDLE SCH  2565931240   
#     28             HOOVER CITY          TRACE CROSSINGS ELEM SCH  2054392700   
#     29             HOOVER CITY                GREYSTONE ELEM SCH  2054393200   
#     30             HOOVER CITY                   HOOVER HIGH SCH  2054391200   
#     31             HOOVER CITY                  BERRY MIDDLE SCH  2054392000   
#     32             HOOVER CITY       SOUTH SHADES CREST ELEM SCH  2054393000   
#     33             HOOVER CITY        ROBERT F BUMPUS MIDDLE SCH  2054392200   
#     34             HOOVER CITY               SPAIN PARK HIGH SCH  2054391400   
#     35             HOOVER CITY              DEER VALLEY ELEM SCH  2054393300   
#     36             HOOVER CITY                 BLUFF PK ELEM SCH  2054392800   
#     37             HOOVER CITY             GREEN VALLEY ELEM SCH  2054392500   
#     38             HOOVER CITY                     GWIN ELEM SCH  2054392600   
#     39             HOOVER CITY          IRA F SIMMONS MIDDLE SCH  2054392100   
#     40             HOOVER CITY              ROCKY RIDGE ELEM SCH  2054392900   
#     41             HOOVER CITY                SHADES MT ELEM SCH  2054393100   
#     42             HOOVER CITY          HOOVER HIGH FRESHMAN CTR  2054391610   
#     43             HOOVER CITY               RIVERCHASE ELEM SCH  2054393400   
#     44             HOOVER CITY      BROCK'S GAP INTERMEDIATE SCH  2054391600   
#     45            MADISON CITY                  HORIZON ELEM SCH  2564643614   
#     46            MADISON CITY              DISCOVERY MIDDLE SCH  2568373735   
#     47            MADISON CITY                BOB JONES HIGH SCH  2567722547   
#     48            MADISON CITY                  MADISON ELEM SCH  2567729255   
#     49            MADISON CITY             WEST MADISON ELEM SCH  2568371189   
#     50            MADISON CITY                 HERITAGE ELEM SCH  2567722075   
#     51            MADISON CITY                  RAINBOW ELEM SCH  2568248106   
#     52            MADISON CITY                LIBERTY MIDDLE SCH  2564300001   
#     53            MADISON CITY                 COLUMBIA ELEM SCH  2564302751   
#     54            MADISON CITY      MILL CREEK ELEMENTARY SCHOOL  3345852012   
#     55  AL INST DEAF AND BLIND           ALABAMA SCHOOL FOR DEAF  2567613214   
#     56  AL INST DEAF AND BLIND          ALABAMA SCHOOL FOR BLIND  2567613259   
#     57  AL INST DEAF AND BLIND               HELEN KELLER SCHOOL  2567613259   
#     58  AL INST DEAF AND BLIND     E H GENTRY TECHNICAL FACILITY  2567613402   
#     59              LEEDS CITY                    LEEDS ELEM SCH  2056994500   
#                            ...                               ...         ...   
#     
#                              MSTREE         MCITY MSTATE   MZIP  MZIP4  \
#     0                  P O BOX 9486    BIRMINGHAM     AL  35220    486   
#     1              315 OUTBACK ROAD       CLAYTON     AL  36016    NaN   
#     2                    P O BOX 66      MT MEIGS     AL  36057    NaN   
#     3                    P O BOX 66      MT MEIGS     AL  36057    NaN   
#     4                    P O BOX 66   MOUNT MEIGS     AL  36057     66   
#     5             8950 ROEBUCK BLVD    BIRMINGHAM     AL  35206   1524   
#     6        1299 HILLSBORO PARKWAY        HELENA     AL  35080    NaN   
#     7             600 E ALABAMA AVE   ALBERTVILLE     AL  35950   2336   
#     8              402 E MCCORD AVE   ALBERTVILLE     AL  35950   2322   
#     9            901 W MCKINNEY AVE   ALBERTVILLE     AL  35950   1346   
#     10               1100 HORTON RD   ALBERTVILLE     AL  35950   2532   
#     11          257 COUNTRY CLUB RD   ALBERTVILLE     AL  35951    NaN   
#     12             1100 HORTON ROAD   ALBERTVILLE     AL  35950    NaN   
#     13                 6077 MAIN ST         GRANT     AL  35747   8333   
#     14               1990 ASBURY RD   ALBERTVILLE     AL  35950    NaN   
#     15     140 CLAYSVILLE SCHOOL RD  GUNTERSVILLE     AL  35976   8454   
#     16                  P O BOX 299       DOUGLAS     AL  35964    NaN   
#     17                  P O BOX 300       DOUGLAS     AL  35964    300   
#     18          2233 SHOAL CREEK RD          ARAB     AL  35016   3510   
#     19                 6077 MAIN ST         GRANT     AL  35747   8333   
#     20          3685 UNION GROVE RD   UNION GROVE     AL  35175   8469   
#     21       12312 US HIGHWAY 431 S  GUNTERSVILLE     AL  35976    NaN   
#     22       12312 US HIGHWAY 431 S  GUNTERSVILLE     AL  35976    NaN   
#     23                  P O BOX 270       DOUGLAS     AL  35964    NaN   
#     24         1050 SCANT CITY ROAD  GUNTERSVILLE     AL  35976   6921   
#     25          994 SCANT CITY ROAD  GUNTERSVILLE     AL  35976    NaN   
#     26                 6077 MAIN ST         GRANT     AL  35747   8333   
#     27                  P O BOX 269       DOUGLAS     AL  35964    269   
#     28           5454 LEARNING LANE        HOOVER     AL  35244   4529   
#     29               300 VILLAGE ST        HOOVER     AL  35242   6447   
#     30         1000 BUCCANEER DRIVE        HOOVER     AL  35244   4511   
#     31              4500 JAGUAR DR.        HOOVER     AL  35242   4698   
#     32      3770 SO SHADES CREST RD        HOOVER     AL  35244   4123   
#     33      1730 LAKE CYRUS CLUB DR        HOOVER     AL  35244    NaN   
#     34            4700 JAGUAR DRIVE        HOOVER     AL  35242    NaN   
#     35     4990 ROSS BRIDGE PARKWAY        HOOVER     AL  35226    NaN   
#     36              569 PARK AVENUE        HOOVER     AL  35226   1218   
#     37       3200 OLD COLUMBIANA RD        HOOVER     AL  35226   3335   
#     38      1580 PATTON CHAPEL ROAD        HOOVER     AL  35226   2299   
#     39      1575 PATTON CHAPEL ROAD        HOOVER     AL  35226   2298   
#     40      2876 OLD ROCKY RIDGE RD        HOOVER     AL  35243   2910   
#     41              2250 SUMPTER ST        HOOVER     AL  35226   3030   
#     42         100 FLEMMING PARKWAY        HOOVER     AL  35244    NaN   
#     43  1950 OLD MONTGOMERY HIGHWAY        HOOVER     AL  35244    NaN   
#     44      1730 LAKE CYRUS CLUB DR        HOOVER     AL  35244    NaN   
#     45        7855 OLD MADISON PIKE       MADISON     AL  35758    NaN   
#     46               1304 HUGHES RD       MADISON     AL  35758    NaN   
#     47                650 HUGHES RD       MADISON     AL  35758    NaN   
#     48                17 COLLEGE ST       MADISON     AL  35758    NaN   
#     49         4976 WALL TRIANA HWY       MADISON     AL  35758    NaN   
#     50         11775 COUNTY LINE RD       MADISON     AL  35758    NaN   
#     51                50 NANCE ROAD       MADISON     AL  35758    NaN   
#     52           281 DOCK MURPHY DR       MADISON     AL  35758    NaN   
#     53               667 BALCH ROAD       MADISON     AL  35758    NaN   
#     54                847 MILL ROAD       MADISON     AL  35758    NaN   
#     55               P O DRAWER 698     TALLADEGA     AL  35160   2411   
#     56                  P O BOX 455     TALLADEGA     AL  35160    NaN   
#     57                  P O BOX 698     TALLADEGA     AL  35161    NaN   
#     58                  P O BOX 698     TALLADEGA     AL  35161    NaN   
#     59            950 ASHVILLE ROAD         LEEDS     AL  35094    NaN   
#                                 ...           ...    ...    ...    ...   
#     
#                           LSTREE         LCITY LSTATE   LZIP  LZIP4      
#     0    RT 2 OLD SPRINGVILLE RD        PINSON     AL  36126    486 ...  
#     1             315 OUTBACK RD       CLAYTON     AL  36016    NaN ...  
#     2       INDUSTRIAL SCHOOL RD      MT MEIGS     AL  36057    NaN ...  
#     3       INDUSTRIAL SCHOOL RD      MT MEIGS     AL  36057    NaN ...  
#     4             I85 SERVICE RD   MOUNT MEIGS     AL  36057     66 ...  
#     5          8950 ROEBUCK BLVD    BIRMINGHAM     AL  35206   1524 ...  
#     6     1299 HILLSBORO PARKWAY        HELENA     AL  35080    NaN ...  
#     7       600 EAST ALABAMA AVE   ALBERTVILLE     AL  35950   2336 ...  
#     8        402 EAST MCCORD AVE   ALBERTVILLE     AL  35950   2322 ...  
#     9      901 WEST MCKINNEY AVE   ALBERTVILLE     AL  35950   1346 ...  
#     10            1100 HORTON RD   ALBERTVILLE     AL  35950   2532 ...  
#     11       257 COUNTRY CLUB RD   ALBERTVILLE     AL  35951    NaN ...  
#     12            1100 HORTON RD   ALBERTVILLE     AL  35950    NaN ...  
#     13              6077 MAIN ST         GRANT     AL  35747   8333 ...  
#     14            1990 ASBURY RD   ALBERTVILLE     AL  35950    NaN ...  
#     15  140 CLAYSVILLE SCHOOL RD  GUNTERSVILLE     AL  35976   8454 ...  
#     16                    HWY 75       DOUGLAS     AL  35964    NaN ...  
#     17                    HWY 75       DOUGLAS     AL  35964    300 ...  
#     18       2233 SHOAL CREEK RD          ARAB     AL  35016   3510 ...  
#     19              6077 MAIN ST         GRANT     AL  35747   8333 ...  
#     20       3685 UNION GROVE RD   UNION GROVE     AL  35175   8469 ...  
#     21    12312 US HWY 431 SOUTH  GUNTERSVILLE     AL  35976    NaN ...  
#     22    12312 US HWY 431 SOUTH  GUNTERSVILLE     AL  35976    NaN ...  
#     23          200 BETHLEHEM RD        HORTON     AL  35950    NaN ...  
#     24        1050 SCANT CITY RD  GUNTERSVILLE     AL  35976   6921 ...  
#     25         994 SCANT CITY RD  GUNTERSVILLE     AL  35976    NaN ...  
#     26              6077 MAIN ST         GRANT     AL  35747   8333 ...  
#     27                    HWY 75       DOUGLAS     AL  35964    269 ...  
#     28          5454 LEARNING LN        HOOVER     AL  35244   4529 ...  
#     29            300 VILLAGE ST        HOOVER     AL  35242   6447 ...  
#     30         1000 BUCCANEER DR        HOOVER     AL  35244   4511 ...  
#     31            4500 JAGUAR DR        HOOVER     AL  35242   2518 ...  
#     32   3770 SO SHADES CREST RD        HOOVER     AL  35244   4123 ...  
#     33   1730 LAKE CYRUS CLUB DR        HOOVER     AL  35244    NaN ...  
#     34            4700 JAGUAR DR        HOOVER     AL  35242    NaN ...  
#     35  4990 ROSS BRIDGE PARKWAY        HOOVER     AL  35226    NaN ...  
#     36              569 PARK AVE        HOOVER     AL  35226   1218 ...  
#     37    3200 OLD COLUMBIANA RD        HOOVER     AL  35226   3335 ...  
#     38     1580 PATTON CHAPEL RD        HOOVER     AL  35226   2299 ...  
#     39     1575 PATTON CHAPEL RD        HOOVER     AL  35226   2298 ...  
#     40   2876 OLD ROCKY RIDGE RD        HOOVER     AL  35243   2910 ...  
#     41           2250 SUMPTER ST        HOOVER     AL  35226   3030 ...  
#     42      100 FLEMMING PARKWAY        HOOVER     AL  35244    NaN ...  
#     43   1950 OLD MONTGOMERY HWY        HOOVER     AL  35244    NaN ...  
#     44   1730 LAKE CYRUS CLUB DR        HOOVER     AL  35244    NaN ...  
#     45       7855 OLD MADISON PK       MADISON     AL  35758    NaN ...  
#     46            1304 HUGHES RD       MADISON     AL  35758    NaN ...  
#     47             650 HUGHES RD       MADISON     AL  35758    NaN ...  
#     48             17 COLLEGE ST       MADISON     AL  35758    NaN ...  
#     49      4976 WALL TRIANA HWY       MADISON     AL  35758    NaN ...  
#     50      11775 COUNTY LINE RD       MADISON     AL  35758    NaN ...  
#     51               50 NANCE RD       MADISON     AL  35758    NaN ...  
#     52        281 DOCK MURPHY DR       MADISON     AL  35758    NaN ...  
#     53              667 BALCH RD       MADISON     AL  35758    NaN ...  
#     54               847 MILL RD       MADISON     AL  35758    NaN ...  
#     55            P O DRAWER 698     TALLADEGA     AL  35160   2411 ...  
#     56         705 EAST SOUTH ST     TALLADEGA     AL  35160    NaN ...  
#     57          1221 COCHRAN AVE     TALLADEGA     AL  35161    NaN ...  
#     58         1105 FORT LASHLEY     TALLADEGA     AL  35160    NaN ...  
#     59           950 ASHVILLE RD         LEEDS     AL  35094    NaN ...  
#                              ...           ...    ...    ...    ...      
#     
#     [103483 rows x 322 columns]

# In[5]:

# del schooldf


# In[9]:

# In[15]:

# NCESid = NCESid.dropna().drop_duplicates().astype(np.int)


# In[31]:

# yesNCES = []
# notNCES = []
# for ID in NCESid:
#     print ID in NCESSCH
#     break
#     if ID in NCESSCH:
#         yesNCES.append(ID)
#     else:
#         notNCES.append(ID)
# 
