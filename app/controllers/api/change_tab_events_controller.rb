class Api::ChangeTabEventsController < ApplicationController
  include TimeHelper
  include Showable
  include Indexable
  include Createable

  private

  def change_tab_event_params
    params.require(:change_tab_event).permit(:id, :session_id, :url, :created_at)
  end
end
