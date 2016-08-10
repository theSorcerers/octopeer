class Api::WindowResolutionEventsController < ApplicationController
  include TimeHelper
  include Showable
  include Indexable
  include Createable

  private

  def window_resolution_event_params
    params.require(:window_resolution_event).permit(:id, :width, :height, :session_id, :created_at)
  end
end
