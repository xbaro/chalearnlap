from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from .forms import UserRegisterForm, UserLoginForm, ChangePassForm, ResetPassForm, SetPassForm, MemberCreationForm
from registration.backends.default.views import RegistrationView, ActivationView
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^home/$', views.home, name="home"),
    # Register, Login, edit password urls (Django auth)
    url(r'^register/$', RegistrationView.as_view(form_class = UserRegisterForm), name = 'register'),
    url(r'^login/$', auth_views.login, {'authentication_form': UserLoginForm}, name = 'auth_login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'home'}, name='auth_logout'),
    url(r'^password/change/$', auth_views.password_change, {'password_change_form': ChangePassForm}, name='auth_password_change'),
    url(r'^password_change/done/$', auth_views.password_change_done, name='password_change_done'),
    url(r'^password_reset/$', auth_views.password_reset, {'password_reset_form': ResetPassForm}, name='auth_password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm, {'set_password_form': SetPassForm}, name='auth_password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^activate/complete/$', TemplateView.as_view(template_name='registration/activation_complete.html'), name='registration_activation_complete'),
    url(r'^activate/(?P<activation_key>\w+)/$', ActivationView.as_view(), name='registration_activate'),
    url(r'^register/complete/$', TemplateView.as_view(template_name='registration/registration_complete.html'), name='registration_complete'),
    url(r'^register/closed/$', TemplateView.as_view(template_name='registration/registration_closed.html'), name='registration_disallowed'),
    # User urls
    url(r'^user/list/$', views.user_list, name="user_list"),
    url(r'^user/edit/(?P<id>\d+)/$', views.user_edit, name="user_edit"),
    url(r'^user/export-csv/$', views.export_user_csv, name="export_user_csv"),
    url(r'^user/export-xls/$', views.export_user_xls, name="export_user_xls"),
    url(r'^user/export-xlsx/$', views.export_user_xlsx, name="export_user_xlsx"),
    # Profile urls (Editors, Organizers...)
    url(r'^profile/edit/(?P<id>\d+)/$', views.profile_edit, name="profile_edit"),
    url(r'^profile/creation/$', views.Backend.as_view(form_class = MemberCreationForm,template_name='registration/registration_form_email.html'), name="profile_creation"),
    # Dataset urls
    url(r'^dataset/list/$', views.dataset_list, name="dataset_list"),
    url(r'^dataset/creation/$', views.dataset_creation, name="dataset_creation"),
    url(r'^dataset/(?P<id>\d+)/edit/$', views.dataset_edit, name="dataset_edit"),
    url(r'^dataset/(?P<id>\d+)/edit/description$', views.dataset_edit_desc, name="dataset_edit_desc"),
    url(r'^dataset/(?P<id>\d+)/edit/schedule$', views.dataset_edit_schedule, name="dataset_edit_schedule"),
    url(r'^dataset/(?P<id>\d+)/edit/associated-events$', views.dataset_edit_relations, name="dataset_edit_relations"),
    url(r'^dataset/(?P<id>\d+)/edit/datas$', views.dataset_edit_datas, name="dataset_edit_datas"),
    url(r'^dataset/(?P<id>\d+)/edit/results/(?P<grid_id>\d+)/$', views.dataset_edit_results, name="dataset_edit_results"),
    url(r'^dataset/(?P<id>\d+)/edit/news$', views.dataset_edit_news, name="dataset_edit_news"),
    url(r'^dataset/(?P<id>\d+)/edit/publications$', views.dataset_edit_publications, name="dataset_edit_publications"),
    # url(r'^dataset/(?P<id>\d+)/edit/(?P<col_id>\d+)/column$', views.dataset_edit_col, name="dataset_edit_col"),
    url(r'^dataset/(?P<id>\d+)/edit/(?P<submission_id>\d+)/submission$', views.dataset_edit_submission, name="dataset_edit_submission"),
    url(r'^dataset/(?P<id>\d+)/edit/members$', views.dataset_edit_members, name="dataset_edit_members"),
    url(r'^dataset/(?P<id>\d+)/publish/$', views.dataset_publish, name="dataset_publish"),
    url(r'^dataset/(?P<id>\d+)/unpublish/$', views.dataset_unpublish, name="dataset_unpublish"),
    url(r'^dataset/(?P<id>\d+)/description/$', views.dataset_desc, name="dataset_desc"),
    url(r'^dataset/(?P<id>\d+)/schedule/$', views.dataset_schedule, name="dataset_schedule"),
    url(r'^dataset/(?P<id>\d+)/publications/$', views.dataset_publications, name="dataset_publications"),
    url(r'^dataset/(?P<id>\d+)/remove/$', views.dataset_remove, name="dataset_remove"),
    # url(r'^dataset/select/(?P<id>\d+)/$', views.dataset_select, name="dataset_select"),
    # Data urls
    url(r'^dataset/(?P<id>\d+)/data/creation/$', views.data_creation, name="data_creation"),
    url(r'^dataset/(?P<dataset_id>\d+)/data/(?P<id>\d+)/remove/$', views.data_remove, name="data_remove"),
    url(r'^dataset/(?P<dataset_id>\d+)/data/(?P<id>\d+)/description/$', views.data_desc, name="data_desc"),
    url(r'^dataset/(?P<dataset_id>\d+)/data/(?P<id>\d+)/software/$', views.data_software, name="data_software"),
    url(r'^dataset/(?P<dataset_id>\d+)/data/(?P<id>\d+)/files/$', views.data_files, name="data_files"),
    url(r'^dataset/(?P<dataset_id>\d+)/data/(?P<id>\d+)/metric/$', views.data_metric, name="data_metric"),
    url(r'^dataset/(?P<dataset_id>\d+)/results/(?P<grid_id>\d+)/$', views.dataset_results, name="dataset_results"),
    url(r'^dataset/(?P<dataset_id>\d+)/data/(?P<id>\d+)/edit/$', views.data_edit, name="data_edit"),
    url(r'^dataset/(?P<dataset_id>\d+)/data/(?P<id>\d+)/edit/description$', views.data_edit_desc, name="data_edit_desc"),
    url(r'^dataset/(?P<dataset_id>\d+)/data/(?P<id>\d+)/edit/files$', views.data_edit_files, name="data_edit_files"),
    url(r'^dataset/(?P<dataset_id>\d+)/data/(?P<id>\d+)/file/creation/$', views.file_creation, name="file_creation"),
    url(r'^dataset/(?P<dataset_id>\d+)/data/(?P<id>\d+)/file/(?P<file_id>\d+)/remove/$', views.file_remove, name="file_remove"),
    url(r'^dataset/(?P<dataset_id>\d+)/data/(?P<id>\d+)/publish/$', views.data_publish, name="data_publish"),
    url(r'^dataset/(?P<dataset_id>\d+)/data/(?P<id>\d+)/unpublish/$', views.data_unpublish, name="data_unpublish"),
    url(r'^dataset/(?P<dataset_id>\d+)/schedule/creation$', views.schedule_creation, name="schedule_creation"),
    url(r'^dataset/(?P<dataset_id>\d+)/schedule/(?P<schedule_id>\d+)/edit/$', views.schedule_edit, name="schedule_edit"),
    url(r'^dataset/(?P<dataset_id>\d+)/schedule/(?P<schedule_id>\d+)/remove/$', views.dataset_schedule_remove, name="dataset_schedule_remove"),
    url(r'^dataset/(?P<dataset_id>\d+)/associated-events/creation$', views.event_relation_creation, name="dataset_associated_events_creation"),
    url(r'^dataset/(?P<dataset_id>\d+)/associated-events/(?P<relation_id>\d+)/remove$', views.event_relation_remove, name="dataset_associated_events_remove"),
    url(r'^dataset/(?P<dataset_id>\d+)/associated-events/$', views.dataset_associated_events, name="dataset_associated_events"),
    url(r'^dataset/(?P<dataset_id>\d+)/news/creation/$', views.news_creation, name="dataset_news_creation"),
    url(r'^dataset/(?P<dataset_id>\d+)/news/(?P<news_id>\d+)/remove$', views.dataset_news_remove, name="dataset_news_remove"),
    url(r'^dataset/(?P<dataset_id>\d+)/submission/(?P<grid_id>\d+)/creation$', views.submission_creation, name="submission_creation"),
    url(r'^dataset/(?P<dataset_id>\d+)/member/select/$', views.dataset_profile_select, name="dataset_profile_select"),
    url(r'^dataset/(?P<dataset_id>\d+)/member/(?P<member_id>\d+)/remove$', views.dataset_member_remove, name="dataset_member_remove"),
    url(r'^dataset/(?P<dataset_id>\d+)/export-participants-csv/$', views.export_participants_csv, name="export_participants_csv"),
    url(r'^dataset/(?P<dataset_id>\d+)/export-submitted-xls/$', views.export_participants_xls, name="export_participants_xls"),
    url(r'^dataset/(?P<dataset_id>\d+)/export-submitted-xlsx/$', views.export_participants_xlsx, name="export_participants_xlsx"),
    url(r'^dataset/(?P<id>\d+)/publication/creation/$', views.publication_creation, name="dataset_publication_creation"),
    url(r'^dataset/(?P<id>\d+)/publication/(?P<pub_id>\d+)/edit/$', views.publication_edit, name="publication_edit"),
    url(r'^dataset/(?P<id>\d+)/publication/(?P<pub_id>\d+)/remove/$', views.publication_remove, name="publication_remove"),
    # Partner urls
    url(r'^partner/list/$', views.partner_list, name="partners_list"),
    url(r'^partner/creation/$', views.partner_creation, name="partner_creation"),
    url(r'^partner/select/(?P<id>\d+)/$', views.partner_select, name="partner_select"),
    # Event urls (Challenge, Workshops...)
    url(r'^event/list/$', views.event_list, name="event_list"),
    url(r'^event/creation/$', views.event_creation, name="event_creation"),
    url(r'^event/(?P<id>\d+)/detail/$', views.event_detail, name="event_detail"),
    url(r'^event/(?P<id>\d+)/remove/$', views.event_remove, name="event_remove"),
    url(r'^event/(?P<id>\d+)/member/select/$', views.profile_select, name="profile_select"),
    url(r'^event/(?P<id>\d+)/member/(?P<member_id>\d+)/remove$', views.event_member_remove, name="event_member_remove"),
    url(r'^event/(?P<id>\d+)/news/(?P<news_id>\d+)/remove$', views.event_news_remove, name="event_news_remove"),
    url(r'^event/(?P<id>\d+)/program/(?P<program_id>\d+)/remove$', views.event_program_remove, name="event_program_remove"),
    url(r'^event/(?P<id>\d+)/schedule/(?P<program_id>\d+)/remove$', views.event_schedule_remove, name="event_schedule_remove"),
    url(r'^event/(?P<id>\d+)/partner/(?P<partner_id>\d+)/remove$', views.event_partner_remove, name="event_partner_remove"),
    url(r'^event/(?P<id>\d+)/associated-events/creation$', views.event_relation_creation, name="event_relation_creation"),
    url(r'^event/(?P<id>\d+)/associated-events/(?P<relation_id>\d+)/remove$', views.event_relation_remove, name="event_relation_remove"),
    url(r'^event/(?P<id>\d+)/associated-events/(?P<relation_id>\d+)/edit$', views.event_relation_edit, name="event_relation_edit"),
    url(r'^event/(?P<id>\d+)/news/creation/$', views.news_creation, name="news_creation"),
    url(r'^event/(?P<id>\d+)/news/(?P<news_id>\d+)/edit/$', views.news_edit, name="news_edit"),
    url(r'^event/(?P<id>\d+)/program/creation/$', views.program_creation, name="program_creation"),
    url(r'^event/(?P<event_id>\d+)/schedule/(?P<schedule_id>\d+)/edit/$', views.schedule_edit, name="schedule_edit"),
    url(r'^event/(?P<event_id>\d+)/program/(?P<program_id>\d+)/edit/$', views.schedule_edit, name="program_edit"),
    url(r'^event/(?P<event_id>\d+)/program/(?P<program_id>\d+)/subevent/creation/$', views.subevent_creation, name="subevent_creation"),
    url(r'^event/(?P<event_id>\d+)/schedule/creation$', views.schedule_creation, name="schedule_creation"),
    url(r'^event/(?P<event_id>\d+)/export-members-csv/$', views.export_members_csv, name="export_members_csv"),
    url(r'^event/(?P<event_id>\d+)/export-members-xls/$', views.export_members_xls, name="export_members_xls"),
    url(r'^event/(?P<event_id>\d+)/export-members-xlsx/$', views.export_members_xlsx, name="export_members_xlsx"),
    # url(r'^event/edit/(?P<id>\d+)/$', views.event_edit, name="event_edit"),
    # url(r'^event/proposal/$', views.event_proposal, name="event_proposal"),
    url(r'^challenge/(?P<id>\d+)/publish/$', views.challenge_publish, name="challenge_publish"),
    url(r'^challenge/(?P<id>\d+)/unpublish/$', views.challenge_unpublish, name="challenge_unpublish"),
    url(r'^challenge/(?P<id>\d+)/edit/description$', views.challenge_edit_desc, name="challenge_edit_desc"),
    url(r'^challenge/(?P<id>\d+)/edit/schedule$', views.challenge_edit_schedule, name="challenge_edit_schedule"),
    url(r'^challenge/(?P<id>\d+)/edit/associated-events$', views.challenge_edit_relation, name="challenge_edit_relation"),
    # url(r'^challenge/(?P<id>\d+)/edit/result$', views.challenge_edit_result, name="challenge_edit_result"),
    url(r'^challenge/(?P<id>\d+)/edit/members$', views.challenge_edit_members, name="challenge_edit_members"),
    url(r'^challenge/(?P<id>\d+)/edit/sponsors$', views.challenge_edit_sponsors, name="challenge_edit_sponsors"),
    url(r'^challenge/(?P<id>\d+)/edit/tracks$', views.challenge_edit_tracks, name="challenge_edit_tracks"),
    url(r'^challenge/(?P<id>\d+)/edit/news$', views.challenge_edit_news, name="challenge_edit_news"),
    url(r'^challenge/(?P<id>\d+)/edit/publications$', views.challenge_edit_publications, name="challenge_edit_publications"),
    # url(r'^challenge/(?P<id>\d+)/result/(?P<result_id>\d+)/edit$', views.result_edit, name="result_edit"),
    # url(r'^challenge/(?P<id>\d+)/result/(?P<result_id>\d+)/remove$', views.result_remove, name="result_remove"),
    url(r'^challenge/(?P<id>\d+)/description/$', views.challenge_desc, name="challenge_desc"),
    url(r'^challenge/(?P<id>\d+)/people/$', views.challenge_members, name="challenge_members"),
    url(r'^challenge/(?P<id>\d+)/sponsors/$', views.challenge_sponsors, name="challenge_sponsors"),
    url(r'^challenge/(?P<id>\d+)/sponsors/creation/$', views.challenge_sponsors_creation, name="challenge_sponsors_creation"),
    # url(r'^challenge/(?P<id>\d+)/result/$', views.challenge_result, name="challenge_result"),
    url(r'^challenge/(?P<id>\d+)/schedule/$', views.challenge_schedule, name="challenge_schedule"),
    url(r'^challenge/(?P<id>\d+)/publications/$', views.challenge_publications, name="challenge_publications"),
    url(r'^challenge/(?P<id>\d+)/associated-events/$', views.challenge_associated_events, name="challenge_associated_events"),
    url(r'^challenge/(?P<id>\d+)/track/(?P<track_id>\d+)/remove$', views.track_remove, name="track_remove"),
    url(r'^challenge/(?P<id>\d+)/track/(?P<track_id>\d+)/description/$', views.track_desc, name="track_desc"),
    url(r'^challenge/(?P<id>\d+)/track/(?P<track_id>\d+)/metrics/$', views.track_metrics, name="track_metrics"),
    url(r'^challenge/(?P<id>\d+)/track/(?P<track_id>\d+)/baseline/$', views.track_baseline, name="track_baseline"),
    url(r'^challenge/(?P<id>\d+)/track/(?P<track_id>\d+)/result/$', views.track_result, name="track_result"),
    url(r'^challenge/(?P<id>\d+)/track/(?P<track_id>\d+)/result/(?P<result_id>\d+)/edit/$', views.result_edit, name="result_edit"),
    url(r'^challenge/(?P<id>\d+)/track/(?P<track_id>\d+)/result/(?P<result_id>\d+)/remove/$', views.result_remove, name="result_remove"),
    url(r'^challenge/(?P<id>\d+)/track/(?P<track_id>\d+)/result/header/(?P<header_id>\d+)/edit/$', views.header_edit, name="header_edit"),
    url(r'^challenge/(?P<id>\d+)/track/(?P<track_id>\d+)/result/new-table/$', views.result_new_table, name="result_new_table"),
    url(r'^challenge/(?P<id>\d+)/track/(?P<track_id>\d+)/result/new-row/$', views.result_new_row, name="result_new_row"),
    url(r'^challenge/(?P<id>\d+)/track/(?P<track_id>\d+)/edit/description/$', views.track_edit_desc, name="track_edit_desc"),    
    url(r'^challenge/(?P<id>\d+)/track/(?P<track_id>\d+)/edit/result/$', views.track_edit_result, name="track_edit_result"),
    url(r'^challenge/(?P<id>\d+)/track/creation/$', views.track_creation, name="track_creation"),
    url(r'^challenge/(?P<id>\d+)/publication/creation/$', views.publication_creation, name="challenge_publication_creation"),
    url(r'^challenge/(?P<id>\d+)/publication/(?P<pub_id>\d+)/edit/$', views.publication_edit, name="publication_edit"),
    url(r'^challenge/(?P<id>\d+)/publication/(?P<pub_id>\d+)/remove/$', views.publication_remove, name="publication_remove"),
    url(r'^workshop/(?P<id>\d+)/publish/$', views.workshop_publish, name="workshop_publish"),
    url(r'^workshop/(?P<id>\d+)/unpublish/$', views.workshop_unpublish, name="workshop_unpublish"),
    url(r'^workshop/(?P<id>\d+)/edit/$', views.workshop_edit, name="workshop_edit"),
    url(r'^workshop/(?P<id>\d+)/edit/description$', views.workshop_edit_desc, name="workshop_edit_desc"),
    url(r'^workshop/(?P<id>\d+)/edit/schedule$', views.workshop_edit_schedule, name="workshop_edit_schedule"),
    url(r'^workshop/(?P<id>\d+)/edit/associated-events$', views.workshop_edit_relations, name="workshop_edit_relations"),
    url(r'^workshop/(?P<id>\d+)/edit/program$', views.workshop_edit_program, name="workshop_edit_program"),
    url(r'^workshop/(?P<id>\d+)/edit/people$', views.workshop_edit_members, name="workshop_edit_members"),
    url(r'^workshop/(?P<id>\d+)/edit/gallery$', views.workshop_edit_gallery, name="workshop_edit_gallery"),
    url(r'^workshop/(?P<id>\d+)/edit/news$', views.workshop_edit_news, name="workshop_edit_news"),
    url(r'^workshop/(?P<id>\d+)/edit/publications$', views.workshop_edit_publications, name="workshop_edit_publications"),
    url(r'^workshop/(?P<id>\d+)/description/$', views.workshop_desc, name="workshop_desc"),
    url(r'^workshop/(?P<id>\d+)/program/$', views.workshop_program, name="workshop_program"),
    url(r'^workshop/(?P<id>\d+)/schedule/$', views.workshop_schedule, name="workshop_schedule"),
    url(r'^workshop/(?P<id>\d+)/associated-events/$', views.workshop_associated_events, name="workshop_associated_events"),
    url(r'^workshop/(?P<id>\d+)/speakers/$', views.workshop_speakers, name="workshop_speakers"),
    url(r'^workshop/(?P<id>\d+)/publications/$', views.workshop_publications, name="workshop_publications"),
    url(r'^workshop/(?P<id>\d+)/gallery/$', views.workshop_gallery, name="workshop_gallery"),
    url(r'^workshop/(?P<id>\d+)/gallery/add$', views.add_gallery_picture, name="add_gallery_picture"),
    url(r'^workshop/(?P<id>\d+)/gallery-picture/(?P<pic_id>\d+)/remove$', views.remove_gallery_picture, name="remove_gallery_picture"),
    url(r'^workshop/(?P<id>\d+)/gallery-picture/(?P<pic_id>\d+)/edit$', views.edit_gallery_picture, name="edit_gallery_picture"),
    url(r'^workshop/(?P<id>\d+)/gallery-picture/remove/$', views.remove_gallery, name="remove_gallery"),
    url(r'^workshop/(?P<id>\d+)/people/creation$', views.speaker_creation, name="speaker_creation"),
    url(r'^workshop/(?P<id>\d+)/people/select$', views.speaker_select, name="speaker_select"),
    url(r'^workshop/(?P<id>\d+)/publication/creation/$', views.publication_creation, name="workshop_publication_creation"),
    url(r'^workshop/(?P<id>\d+)/publication/(?P<pub_id>\d+)/edit/$', views.publication_edit, name="publication_edit"),
    url(r'^workshop/(?P<id>\d+)/publication/(?P<pub_id>\d+)/remove/$', views.publication_remove, name="publication_remove"),
    url(r'^workshop/(?P<id>\d+)/sponsors/$', views.workshop_sponsors, name="workshop_sponsors"),
    url(r'^workshop/(?P<id>\d+)/edit/sponsors$', views.workshop_edit_sponsors, name="workshop_edit_sponsors"),
    url(r'^workshop/(?P<id>\d+)/sponsors/creation/$', views.workshop_sponsors_creation, name="workshop_sponsors_creation"),
    url(r'^special-issue/(?P<id>\d+)/publish/$', views.special_issue_publish, name="special_issue_publish"),
    url(r'^special-issue/(?P<id>\d+)/unpublish/$', views.special_issue_unpublish, name="special_issue_unpublish"),
    url(r'^special-issue/(?P<id>\d+)/edit/$', views.special_issue_edit, name="special_issue_edit"),
    url(r'^special-issue/(?P<id>\d+)/edit/description$', views.special_issue_edit_desc, name="special_issue_edit_desc"),
    url(r'^special-issue/(?P<id>\d+)/edit/associated-events$', views.special_issue_edit_relations, name="special_issue_edit_relations"),
    url(r'^special-issue/(?P<id>\d+)/edit/schedule$', views.special_issue_edit_schedule, name="special_issue_edit_schedule"),
    url(r'^special-issue/(?P<id>\d+)/edit/people$', views.special_issue_edit_members, name="special_issue_edit_members"),
    url(r'^special-issue/(?P<id>\d+)/edit/news$', views.special_issue_edit_news, name="special_issue_edit_news"),
    url(r'^special-issue/(?P<id>\d+)/edit/publications$', views.special_issue_edit_publications, name="special_issue_edit_publications"),
    url(r'^special-issue/(?P<id>\d+)/description/$', views.special_issue_desc, name="special_issue_desc"),
    url(r'^special-issue/(?P<id>\d+)/people/$', views.special_issue_members, name="special_issue_members"),
    url(r'^special-issue/(?P<id>\d+)/creation/$', views.special_issue_members, name="special_issue_members"),
    url(r'^special-issue/(?P<id>\d+)/schedule/$', views.special_issue_schedule, name="special_issue_schedule"),
    url(r'^special-issue/(?P<id>\d+)/associated-events/$', views.special_issue_associated_events, name="special_issue_associated_events"),
    url(r'^special-issue/(?P<id>\d+)/publications/$', views.special_issue_publications, name="special_issue_publications"),
    url(r'^special-issue/(?P<id>\d+)/publication/creation/$', views.publication_creation, name="issue_publication_creation"),
    url(r'^special-issue/(?P<id>\d+)/publication/(?P<pub_id>\d+)/edit/$', views.publication_edit, name="publication_edit"),
    url(r'^special-issue/(?P<id>\d+)/publication/(?P<pub_id>\d+)/remove/$', views.publication_remove, name="publication_remove"),
    # url(r'^special-issue/(?P<id>\d+)/papers/$', views.special_issue_papers, name="special_issue_papers"),
    # url(r'^special-issue/(?P<id>\d+)/papers/creation/$', views.papers_creation, name="papers_creation"),
    # url(r'^special-issue/(?P<id>\d+)/papers/(?P<paper_id>\d+)/edit/$', views.papers_edit, name="papers_edit"),
    # url(r'^special-issue/(?P<id>\d+)/papers/(?P<paper_id>\d+)/remove/$', views.papers_remove, name="papers_remove"),
    # Role urls
    url(r'^role/creation/$', views.role_creation, name="role_creation"),
    url(r'^event-proposal/creation/$', views.event_proposal_creation, name="event_proposal_creation"),
    url(r'^event-proposal/list/$', views.event_proposal_list, name="event_proposal_list"),
    url(r'^event-proposal/(?P<id>\d+)/detail/$', views.event_proposal_detail, name="event_proposal_detail"),
    url(r'^event-proposal/(?P<id>\d+)/confirm/$', views.event_proposal_confirm, name="event_proposal_confirm"),
    # Publication urls
    url(r'^publication/creation/$', views.publication_creation, name="publication_creation"),
    url(r'^publication/list/$', views.publication_list, name="publication_list"),
    url(r'^publication/(?P<id>\d+)/detail/$', views.publication_detail, name="publication_detail"),
    url(r'^publication/(?P<pub_id>\d+)/edit/$', views.publication_edit, name="publication_edit"),
    url(r'^publication/(?P<pub_id>\d+)/remove/$', views.publication_remove, name="publication_remove"),
    # Schedule event urls
    # url(r'^schedule/creation/(?P<id>\d+)/$', views.schedule_creation, name="schedule_creation"),
    # url(r'^schedule/creation/(?P<workshop_id>\d+)/(?P<event_id>\d+)/subevent$', views.subevent_creation, name="subevent_creation"),
    # url(r'^schedule/edit/(?P<id>\d+)/$', views.schedule_edit, name="schedule_edit"),
]